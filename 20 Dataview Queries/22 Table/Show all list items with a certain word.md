---
description: Print all Bullet Points that contain a certain word
---
#dataviewquery
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/icontains 

# Show all list items with a certain word

## Basic 

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
```

## Variants

### Group items by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
GROUP BY file.link
```