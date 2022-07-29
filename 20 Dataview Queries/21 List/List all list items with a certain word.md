---
description: List all bullet points that contain a specific word
querytype: LIST
datacommands:
  - FROM
  - WHERE
  - GROUP BY
  - FLATTEN
dqlfunctions:
  - icontains
---
#dataviewquery

# List all list items with a certain word
## Basic 

List all bullet points that contain the word "ipsum"

```dataview
LIST L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
```

## Variants

### list without file link

```dataview
LIST WITHOUT ID L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
```

### list - grouping by file

```dataview
LIST rows.L.text
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE icontains(L.text, "ipsum")
GROUP BY file.link
```