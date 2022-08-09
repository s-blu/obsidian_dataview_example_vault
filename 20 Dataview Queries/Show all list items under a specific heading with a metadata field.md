---
description: Show all bullet points that are in a specific section and have a certain metadata value
---
#dataviewquery
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/meta #dv/contains 

# Show all list items under a specific heading with a metadata field

## Basic 

All lists inside the section "Topics" with "Nickname" in the inline field `author::`

```dataview
TABLE L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Topics"
WHERE contains(L.author, "Nickname")
```

## Variants

### grouping by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Topics"
WHERE contains(L.author, "Nickname")
GROUP BY file.link
```
