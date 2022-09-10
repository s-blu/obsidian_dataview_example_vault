---
description: Shows a table with all open project and a emoji score how long these projects are already open
topics:
  - emoji 
  - scores
---
#dv/table #dv/from #dv/where #dv/date #dvjs/where #dvjs/pages #dvjs/mutate #dvjs/table #dv/dataviewjs 

# List all open projects with a emoji age indicator

## Basic 

```dataview
TABLE "😡" * (date(now) - date(started)).weeks AS "Score"
FROM "10 Example Data/projects"
WHERE status != "finished"
```

## Variants

### Use different emojis for certain timespans

```dataviewjs
const projects = dv.pages('"10 Example Data/projects"')
	.where(p => p.status != "finished")
	.mutate(p => {
		p.age = dv.luxon.Duration.fromMillis(Date.now() - p.started.toMillis())
		p.emojiAgeScore = getEmojiScore(p)
	})

dv.table(["Score", "Project", "Started", "Age"], projects.map(p => [p.emojiAgeScore, p.file.link, p.started, p.age.toFormat("y'y' M'm' w'w'")]))

function getEmojiScore(p) {
	const age = p.age.shiftTo('months').toObject()
	let score = "";
	
	score += addEmojis("👿", age.months / 6)  
	score += addEmojis("😡", (age.months % 6) / 3)
	score += addEmojis("😒", (age.months % 6 % 3)) 

	return score;
}

function addEmojis(emoji, max) {
	let emojis = "";
	for (let i = 1; i < max; i++) emojis += emoji;
	return emojis;
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
dv.view('00 Meta/dataview_views/usedInAUseCase',  { current: dv.current() })
```