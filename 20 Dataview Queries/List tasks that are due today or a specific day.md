---
description: List all tasks that have a duedate (a meta data) set and are due to a specific date or before
topics:
  - task tracking
  - dailies
---
 #dv/TASK #dv/WHERE #dv/date #dv/contains

# List tasks that are due today or a specific day

## Basic 

> [!info] Usage in daily notes
> When used in a daily note thats named in format `YYYY-MM-DD`, you can replace the specific date information (`date("2022-11-30")`) with `this.file.day`
```dataview
TASK 
WHERE !completed AND duedate AND duedate <= date("2022-11-30") AND contains(text, "due")
```

## Variants

### Show tasks that are due today or earlier

```dataview
TASK 
WHERE !completed AND duedate AND duedate <= date(today) AND contains(text, "due")
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
