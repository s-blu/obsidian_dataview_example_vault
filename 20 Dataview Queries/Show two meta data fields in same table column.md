---
description: Show multiple meta data fields in one table column - useful when you need to take renamed fields into account
topics:
  - vault maintenance
---
#dv/table #dv/from #dv/where #dv/flatten #dv/filter

# Show two metadatas in same table column

## Basic 

```dataview
TABLE wake-up, [go-to-sleep, gotosleep] as "Bed time", [lunch, dinner] AS "Meal times"
from "10 Example Data/dailys"
where date(day).weekyear = 3
```

## Variants

In case you only have one valid value per file for this column that is stored in different meta data fields, use filter and flatten:

```dataview
TABLE wake-up, ST AS "Bed time", [lunch, dinner] AS "Meal times"
from "10 Example Data/dailys"
where date(day).weekyear = 3
FLATTEN filter([gotosleep, go-to-sleep], (x) => x) as ST
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