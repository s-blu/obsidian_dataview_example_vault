---
description: Show all bullet points that contain a certain tag
topics:
  - filter bullet points
---
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/contains 

# Show list items containing a certain tag

## Basic 

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tag1")
```

## Variants
### grouping by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tag1")
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
dv.view('00 Meta/dataview_views/usedInAUseCase',  { current: dv.current() })
```