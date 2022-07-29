---
description: Show all bullet points that contain a certain metadata value
querytype: TABLE
datacommands:
  - FROM
  - WHERE
  - FLATTEN
dqlfunctions:
  - contains
---
#dataviewquery

# Show all list items containing a specific metadata value

## Basic

All lists with "Surname" in the inline field `author::`

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.author, "Surname")
```


