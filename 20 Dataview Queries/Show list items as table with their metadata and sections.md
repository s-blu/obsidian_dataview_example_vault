---
description: Show a bullet point list as a table with their metadata and sections (headers) as columns
topics:
  - lists with metadata
---
#dv/table #dv/from #dv/flatten #dv/sort #dv/regexreplace

# Show list items as table with their metadata and sections

## Basic 

```dataview
TABLE WITHOUT ID L.text AS "Food", L.best-before AS "Best before ⬇"
FROM "10 Example Data/food/Food pantry"
FLATTEN file.lists AS L
SORT L.best-before
```

## Variants

### Show the headings they belong to as a column

```dataview
TABLE WITHOUT ID L.text AS "Food", meta(L.section).subpath AS "Type", L.best-before AS "Best before ⬇"
FROM "10 Example Data/food/Food pantry"
FLATTEN file.lists AS L
SORT L.best-before
```

### Remove meta data from bullet point text

```dataview
TABLE WITHOUT ID regexreplace(L.text, "\[best-before:: [0-9-]+\]", "") AS "Food", meta(L.section).subpath AS "Type", L.best-before AS "Best before ⬇"
FROM "10 Example Data/food/Food pantry"
FLATTEN file.lists AS L
SORT L.best-before
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