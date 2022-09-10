---
description: Show all bullet points that contain a certain metadata value
topics:
  - filter bullet points
---
#dv/table #dv/from #dv/where #dv/flatten #dv/contains 

# Show all list items containing a specific metadata value

## Basic

All lists with "Surname" in the inline field `author::`

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.author, "Surname")
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
