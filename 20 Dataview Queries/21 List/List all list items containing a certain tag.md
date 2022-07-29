---
description: List all bullet points that contain a certain tag
---
#dataviewquery
#dv/list #dv/from #dv/where #dv/flatten #dv/contains

# List all list items containing a certain tag

## Basic 

```dataview
LIST WITHOUT ID L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tag1")
```