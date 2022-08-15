---
description: Show all bullet points that contain a certain metadata value
topics:
  - filter bullet points
---
#dataviewquery
#dv/table #dv/from #dv/where #dv/flatten #dv/contains 

# Show all list items containing a specific metadata value

## Basic

All lists with "Surname" in the inline field `author::`

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.author, "Surname")
```


