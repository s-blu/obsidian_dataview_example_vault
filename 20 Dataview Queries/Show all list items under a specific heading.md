---
description: List all bullet points under a certain heading
---
#dataviewquery
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/meta

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
