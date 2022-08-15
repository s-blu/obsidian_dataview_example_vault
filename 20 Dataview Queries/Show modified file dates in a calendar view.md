---
description: Show on which date which files were edited
topics:
  - visualization
---
#dv/calendar

# Show modified file dates in a calendar view

## Basic 

```dataview
CALENDAR file.mtime
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