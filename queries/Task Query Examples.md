# Task Query Examples

List all tasks that are completed for a specific week
```dataview
TASK
FROM "example_data/dailys"
WHERE completed AND date(file.name).week = 5
```


List all tasks with a specific status grouped by their file
```dataview
TASK
FROM "example_data/dailys"
WHERE status = ">"
GROUP BY file.name
```

