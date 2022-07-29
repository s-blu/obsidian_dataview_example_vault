---
description: List all tasks that have a custom status (i.e. >)
---
#dv/task #dv/from #dv/where #dv/sort #dv/limit #dv/groupby 
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