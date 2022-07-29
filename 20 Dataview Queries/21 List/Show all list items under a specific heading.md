---
description: List all bullet points under a certain heading
querytype: TABLE
datacommands:
  - FROM
  - WHERE
  - GROUP BY
  - FLATTEN
dqlfunctions:
  - meta
---
#dataviewquery

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
