---
description: Show all bullet points that contain a certain tag
---
#dataviewquery
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/contains 

# Show list items containing a certain tag

## Basic 

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tag1")
```

## Variants
### grouping by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tag1")
GROUP BY file.link
```
