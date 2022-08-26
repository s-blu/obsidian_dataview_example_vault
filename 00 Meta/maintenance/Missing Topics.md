# Queries with missing topics field

```dataview
LIST 
FROM "20 Dataview Queries" AND !"20 Dataview Queries/21 MOCs"
WHERE !topics OR (length(topics) = 1 AND contains(topics, null))
```

> [!info] Used query
> You want this fancy query for your own data? Find it [[List all files with missing category tag or empty meta data field|here]].