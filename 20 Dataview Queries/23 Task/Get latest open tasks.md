---
description: Get the latest, not completed tasks 
---

#querytype/TASK
#datacommand/FROM  #datacommand/WHERE #datacommand/SORT #datacommand/LIMIT 
# Get latest open tasks

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