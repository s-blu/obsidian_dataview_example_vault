---
description: List all bullet points under a certain heading
topics:
  - filter bullet points
---
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/meta #dv/filter

# Show all list items under a specific heading

## Basic 

All lists inside the section "Research"

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Research"
```

## Variants
### grouping by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Research"
GROUP BY file.link
```

### Using flatten/filter instead of group-by

```dataview
TABLE WITHOUT ID "<nobr>" + file.link + "</nobr>" AS Page, Research
FROM "10 Example Data/dailys"
FLATTEN list(filter(file.lists, (x) => meta(x.section).subpath = "Research").text) as Research
WHERE Research
```

### Using flatten to make multiple columns based on different headings

```dataview
TABLE WITHOUT ID "<nobr>" + file.link + "</nobr>" AS Page, Research, Topics
FROM "10 Example Data/dailys"
FLATTEN list(filter(file.lists, (x) => meta(x.section).subpath = "Research").text) as Research
FLATTEN list(filter(file.lists, (x) => meta(x.section).subpath = "Topics").text) as Topics
WHERE Research OR Topics
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