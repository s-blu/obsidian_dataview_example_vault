---
description: List all tasks that have a custom status (i.e. >)
topics:
  - custom status for tasks
---
#dv/task #dv/from #dv/where #dv/sort #dv/limit #dv/groupby 
# List all tasks with a custom status

## Basic 

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE status = ">"
```

## Variants

Show only the most recent 5 todos grouped after their file day

> [!hint] 
> The first SORT (`SORT file.day DESC`) sorts the TASKS you're getting so you have the most recent at top. The second SORT (`rows.file.day DESC`) sorts your groups to have Feb 5 at the top instead of Jan 30 - try removing it!

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE status = ">"
SORT file.day DESC
LIMIT 5
GROUP BY file.day
SORT rows.file.day DESC
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