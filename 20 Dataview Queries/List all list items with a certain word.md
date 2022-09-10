---
description: List all bullet points that contain a specific word
topics:
  - filter bullet points
---
#dv/list #dv/from #dv/where #dv/groupby #dv/flatten #dv/icontains

# List all list items with a certain word
## Basic 

List all bullet points that contain the word "ipsum"

```dataview
LIST L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
```

## Variants

### list without file link

```dataview
LIST WITHOUT ID L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
```

### list - grouping by file

```dataview
LIST rows.L.text
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