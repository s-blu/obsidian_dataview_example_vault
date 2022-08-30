---
description: Show all bullet points that are in a specific section and have a certain metadata value
topics:
  - filter bullet points
---
#dataviewquery
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/meta #dv/contains 

# Show all list items under a specific heading with a metadata field

## Basic 

All lists inside the section "Topics" with "Nickname" in the inline field `author::`

```dataview
TABLE L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Topics"
WHERE contains(L.author, "Nickname")
```

## Variants

### grouping by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Topics"
WHERE contains(L.author, "Nickname")
GROUP BY file.link
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