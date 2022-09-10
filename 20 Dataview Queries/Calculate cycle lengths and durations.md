---
description: Calculate cycle times and durations based on meta data value in your dailies, i.e. how long your maniac phase or migraine holds
topics:
  - timespans
  - durations
---
#dv/dataviewjs #dvjs/pages #dvjs/mutate #dvjs/duration #dvjs/luxon #dvjs/sort #dvjs/array #dvjs/table 

# Calculate cycle lengths and durations

## Basic 

```dataviewjs
const metadatafield = ""

let startDates = dv.pages('"10 Example Data/dailys"').mutate(p => p.previousDay = dv.page(dv.luxon.DateTime.fromMillis(p.file.day - dv.duration("1d")).toFormat('yyyy-MM-dd'))).sort(p => p.file.name)

const endDates = dv.array(dv.clone(startDates)[0]).where(p => !checkCriteria(p) && checkCriteria(p.previousDay))

startDates = startDates.where(p => checkCriteria(p) && !checkCriteria(p.previousDay))

const cycles = [];
for (let i = 0; i < endDates.length; i++) {
	cycles.push([
		startDates[i].file.link,
		endDates[i].file.link,
		dv.luxon.Duration.fromMillis(endDates[i].file.day - startDates[i].file.day),
		i === 0 ? '' : dv.luxon.Duration.fromMillis(startDates[i].file.day - endDates[i-1]?.file.day),
		i === 0 ? '' : dv.luxon.Duration.fromMillis(startDates[i].file.day - startDates[i-1]?.file.day).toFormat("d 'Days'"),
	])
}

dv.table(["Start", "End", "Duration", "Gap", "Cycletime"], cycles)

function checkCriteria(p) {
	return p && p.wellbeing && (p.wellbeing["pain-type"] || []).contains("head")
}

```

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
await dv.view('00 Meta/dataview_views/usedInAUseCase', {current: dv.current()})
```