---
description: Get the latest, not completed tasks 
topics:
  - open tasks
  - latest items
---
#dataviewquery
#dv/task #dv/from #dv/where #dv/sort #dv/limit 

# Get latest open tasks

> [!info] Difference between status and completed
> A task only counts as completed if its status is equals to "x". If you use custom task statuses, i.e. "-", a task will appear checked but is _not_ completed.

## Basic 

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE !completed
SORT file.day DESC
LIMIT 10
```

## Variants

If using custom statuses for TASKS, it's maybe better to check for `status = " "` instead of `!completed`, depending on your use case 

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE status = " "
SORT file.day DESC
LIMIT 10
```