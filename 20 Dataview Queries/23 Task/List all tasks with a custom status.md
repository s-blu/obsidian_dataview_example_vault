---
description: List all tasks that have a custom status (i.e. >)
---

#querytype/TASK
#datacommand/FROM  #datacommand/WHERE #datacommand/SORT #datacommand/GROUPBY #datacommand/LIMIT 
# List all tasks with a custom status

## Basic 

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE status = ">"
```

## Variants

Show only the most recent 5 todos grouped after their file day

> [!attention] The sorting doesn't work like expected, for some reason 🙈

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE status = ">"
SORT file.day DESC
LIMIT 5
GROUP BY day
```