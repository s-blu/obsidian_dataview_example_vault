---
description: Fetches the file that has the highest day that is lower than the current files day in order to get the previous day
topics:
  - navigation
date: 2022-07-07
---
#dv/list #dv/from #dv/where #dv/sort #dv/limit 

# Get a link to the previous daily (not necessarily yesterday)

## Basic 

```dataview
LIST WITHOUT ID
FROM "10 Example Data/dailys"
WHERE file.name != this.file.name AND file.day < this.file.day
SORT file.day DESC
LIMIT 1
```

## Variants
### Show a custom prefix before the link

```dataview
LIST WITHOUT ID t
FROM "10 Example Data/dailys"
WHERE file.name != this.file.name AND file.day < this.file.day
SORT file.day DESC
FLATTEN "Previous day: " + file.link AS t
LIMIT 1
```

### Get a link to the next day with a daily note

```dataview
LIST WITHOUT ID t
FROM "10 Example Data/dailys"
WHERE file.name != this.file.name AND file.day > this.file.day
SORT file.day ASC
FLATTEN "Next day: " + file.link AS t
LIMIT 1
```

> [!help]- Similar Queries
> Maybe these queries are of interest for you, too:
> ```dataview
> LIST
> FROM "20 Dataview Queries"
> FLATTEN topics as flattenedTopics
> WHERE contains(this.topics, flattenedTopics)
> AND file.name != this.file.name
> ```