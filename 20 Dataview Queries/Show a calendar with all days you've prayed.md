---
description: Show a calender that marks all days with praying = yes
topics:
  - habit tracking
---
#dv/table #dv/from #dv/where 

# Show a calendar with all days you've prayed

## Basic 

> [!info]
> You'll need to go back to Januray/Februrary 2022 to see the data.

```dataview
CALENDAR file.day
FROM "10 Example Data/dailys"
WHERE praying = "yes"
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