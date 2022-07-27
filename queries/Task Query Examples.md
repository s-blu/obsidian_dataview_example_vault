# Task Query Examples

List all tasks with a specific status
```dataview
TASK
FROM "example_data/dailys"
WHERE status = ">"
```

---

Get latest 10 uncompleted (status is not "x") tasks
```dataview
TASK
FROM "example_data/dailys"
WHERE !completed
SORT file.day DESC
LIMIT 10
```

---

Get latest 10 tasks with a status (not empty) grouped by their status
```dataview
TASK FROM "example_data/dailys" 
WHERE status != " "
SORT file.day DESC 
LIMIT 10
GROUP BY status 
```