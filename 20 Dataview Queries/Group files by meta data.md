---
description: Display Files grouped after metadata where one felt discomfort
topics:
  - grouping
  - group pages based on meta data
---
#dv/table #dv/from #dv/where #dv/groupby #dv/choice 
# Group files by meta data

## Basic 

```dataview
TABLE rows.file.link, rows.wellbeing.pain-type
FROM #daily 
WHERE wellbeing.mood-notes = "discomfort"
GROUP BY wellbeing.pain
```
## Variants

Add better readable table headers

```dataview
TABLE WITHOUT ID row.key AS "Pain", rows.file.link AS "Dailys", rows.wellbeing.pain-type AS "Type of Pain"
FROM #daily 
WHERE wellbeing.mood-notes = "discomfort"
GROUP BY wellbeing.pain
```

---

Replace pain numbers with textual information

```dataview
TABLE WITHOUT ID choice(row.key = 0, "None", choice(row.key = 1, "Little", choice(row.key = 2, "Middle", choice(row.key = 3, "High", row.key))))  AS "Pain", rows.file.link AS "Dailys", rows.wellbeing.pain-type AS "Type of Pain"
FROM #daily 
WHERE wellbeing.mood-notes = "discomfort"
GROUP BY wellbeing.pain
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
const inlinksFromUseCases = dv.current().file.inlinks.filter(link => link.path.contains("33 Use Cases"));

const header = `> [!info] Part of Use Cases`;

if (inlinksFromUseCases.length > 1) {
	const list = inlinksFromUseCases.array().reduce((acc, curr) => `${acc}</br> - ${curr}`,"")

	dv.span(`${header}
    > This query is part of following use cases:
    > ${list}
    > 
	`)
} else if (inlinksFromUseCases.length === 1) {
	dv.span(`${header}
    > This query is part of use case ${inlinksFromUseCases[0]}.
	`)
}
```