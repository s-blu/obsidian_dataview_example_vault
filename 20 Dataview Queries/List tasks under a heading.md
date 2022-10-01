---
description: Lists tasks under a heading. Useful if you have i.e. a "Urgent" heading in project files
topics:
  - task tracking
  - dailies
---
 #dv/TASK #dv/FROM #dv/meta #dv/WHERE #dv/date

# List tasks under a heading

## Basic 

```dataview
TASK 
FROM "10 Example Data/projects" 
WHERE meta(section).subpath = "Urgent"
```

## Variants

### List tasks from a certain daily

```dataview
TASK 
FROM "10 Example Data/dailys" 
WHERE file.day = date("2022-02-16") AND meta(section).subpath = "Gonna do this tmrw"
```
```dataview
TASK 
FROM "10 Example Data/dailys" 
WHERE file.day = date("2022-02-16") AND meta(section).subpath = "Gonna do this tmrw"
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
