# Queries with incomplete processed template

## Query Pages with unmaintained tags

```dataview
LIST
FROM "20 Dataview Queries"
WHERE econtains(file.etags, "#dv/")
```

## Query Pages with the ToDo callout

```dataview
LIST
FROM "20 Dataview Queries"
WHERE contains(file.tasks.text, "Use this template")
```