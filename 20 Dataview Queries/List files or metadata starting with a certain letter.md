---
description: List filenames or files with metadata values that start with a specific character
topics:
  - filter for filenames
---
#dv/list #dv/from #dv/where 

# List files or metadata starting with a certain letter

## Basic 

For filenames:
```dataview
LIST
FROM "10 Example Data"
WHERE file.name[0] = "A"
```

For metadata fields:

```dataview
LIST
FROM "10 Example Data"
WHERE author[0] = "B"
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