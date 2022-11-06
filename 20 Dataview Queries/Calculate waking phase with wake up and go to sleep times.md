---
description: Calculate time spans with a start and end time, i.e. waking phase by wake up and go to sleep times
topics: 
  - durations
  - timespans
---
#dv/dataviewjs #dv/table #dv/from #dv/limit #dv/flatten #dvjs/pages #dvjs/limit #dvjs/mutate #dvjs/table #dvjs/map #dvjs/luxon 

# Calculate waking phase with wake up and go to sleep times
## Basic 
### As DataviewJS solution
```dataviewjs
const dailies = dv.pages('"10 Example Data/dailys"')
	.limit(10)
	.mutate(p => p.wakingPhase = calculateWakingPhase(p["wake-up"], p["go-to-sleep"]))


dv.table(["File", "wake-up", "go-to-sleep", "Waking Phase"], 
		 dailies.map(p => [p.file.link, p["wake-up"], p["go-to-sleep"], p.wakingPhase]))

function calculateWakingPhase(wakeUp, goToSleep) {
	const isValid = isValidTime(wakeUp) && isValidTime(goToSleep)
	if (!isValid) return '_⚠ Input times not valid_'
	
	wakeUp = dv.luxon.Duration.fromISOTime(wakeUp);
	goToSleep = dv.luxon.Duration.fromISOTime(goToSleep);
	return dv.luxon.Duration.fromMillis(goToSleep - wakeUp) 
}

function isValidTime(time) {
	const dur = dv.luxon.Duration.fromISOTime(time);
	return !dur.invalid;
}
```

### As DQL (dataview) solution
> [!attention] Dates with invalid times will be skipped and file.day (or another metadata with the files date) must be set 

```dataview
TABLE wake-up, go-to-sleep, wakeTime
FROM "10 Example Data/dailys"
LIMIT 10
FLATTEN dateformat(file.day, "yyyy-MM-dd") as dt
FLATTEN date(dt + "T" + go-to-sleep) - date(dt + "T" + wake-up) as wakeTime
```

## Variants

### Calculate Sleeping time instead Wake time

```dataview
TABLE go-to-sleep, wake-up, sleep
FROM "10 Example Data/dailys"
LIMIT 10
FLATTEN dateformat(file.day, "yyyy-MM-dd") as dt
FLATTEN (date(dt + "T" + wake-up) + dur("1d")) - date(dt + "T" + go-to-sleep)  as sleep
```

## Variants


### Fix up missing leading zeros & sleep times after midnight

```dataviewjs
const Duration = dv.luxon.Duration;
const dailies = dv.pages('"10 Example Data/dailys"')
	.limit(10)
	.mutate(p => p.wakingPhase = calculateWakingPhase(p["wake-up"], p["go-to-sleep"]))


dv.table(["File", "wake-up", "go-to-sleep", "Waking Phase"], dailies.map(p => [p.file.link, p["wake-up"], p["go-to-sleep"], p.wakingPhase]))

function calculateWakingPhase(wakeUp, goToSleep) {
	wakeUp = tryToFixUp(wakeUp);
	goToSleep = tryToFixUp(goToSleep);
	
	const isValid = isValidTime(wakeUp) && isValidTime(goToSleep)
	if (!isValid) return '_⚠ Input times not valid_'
	
	wakeUp = Duration.fromISOTime(wakeUp);
	goToSleep = Duration.fromISOTime(goToSleep);
	if (goToSleep < wakeUp) {
		goToSleep = goToSleep.plus(Duration.fromISO("P1D"))
	}
	return Duration.fromMillis(goToSleep - wakeUp) 
}

function tryToFixUp(time) {
	if (!time) return time;
	if (time.match(/^[0-9]{3}/) || time.match(/^[0-9]{1}:[0-9]{2}/)) {
		return "0" + time;
	}
	return time;
}

function isValidTime(time) {
	return !Duration.fromISOTime(time).invalid;
}
```

### Calculation with 00h00m format

If your metadata has the format `00h00m`, i.e. `15h55m`, calculations get easier.

t1:: 11h45m
t2:: 15h55m

```dataview
TABLE WITHOUT ID t1, t2, duration
WHERE file.name = this.file.name
FLATTEN t2 - t1 as duration
```

### As Inline statement for current file

date:: 2022-06-06
wake-up:: 07:35
go-to-sleep:: 23:50

Wake time: `= date(dateformat(this.file.day, "yyyy-MM-dd") + "T" + this.go-to-sleep) - (date(dateformat(this.file.day, "yyyy-MM-dd") + "T" + this.wake-up))`

---
%% === end of query page === %%
> [!help]- Similar Queries
> Maybe these queries are of interest for you, too:
> ```dataview
> LIST
> FROM "20 Dataview Queries"
> FLATTEN topics as flattenedTopics
> WHERE contains(this.topics, flattenedTopics)
> AND file.name != this.file.name
> ```

```dataviewjs
dv.view('00 Meta/dataview_views/usedInAUseCase',  { current: dv.current() })
```