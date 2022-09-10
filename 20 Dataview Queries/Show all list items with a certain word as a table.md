---
description: Print all Bullet Points that contain a certain word
topics:
  - filter bullet points
---
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/icontains 

# Show all list items with a certain word as a table

## Basic 

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
```

## Variants

### Group items by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
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