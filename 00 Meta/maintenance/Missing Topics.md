# Queries with missing topics field

```dataview
LIST 
FROM "20 Dataview Queries" AND !"20 Dataview Queries/21 MOCs"
WHERE !topics OR (length(topics) = 1 AND contains(topics, null))
```