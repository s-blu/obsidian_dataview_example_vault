---
description: List all bullet points from a certain date while ignoring the year, i.e. for "today last year" retrospectives
topics:
  - dailies
  - bullet points filtering
---
 #dv/LIST #dv/WHERE #dv/dateformat

# List bullet points from dailys of a specific date without year

## Basic 

```dataview
LIST file.lists.text
WHERE dateformat(file.day, "MM-dd") = "02-17"
```

## Variants

### Description of Variant A - what does it differently? What do we achieve with that?

> [!info] Usage in dailies
> When used in a daily and your dailies are named in format `YYYY-MM-DD`, the part  `AND file.day.year != this.file.day.year` will filter out the bullet points of the daily currently open. In the case of this example file it doesnt do anything, though. See [[2022-02-17]] for a working example.

```dataview
LIST file.lists.text
WHERE dateformat(file.day, "MM-dd") = "02-17" AND file.day.year != this.file.day.year
```
---
%% === end of query page === %%
> [!help]- Similar Queries
> Maybe these queries are of interest for you, too:
> ```dataview
> LIST
> FROM "20 Dataview Queries"
> FLATTEN topics as flattenedTopics
> WHERE contains(this.topics, flattenedTopics)
> AND file.name != this.file.name
> ```

```dataviewjs
dv.view('00 Meta/dataview_views/usedInAUseCase',  { current: dv.current() })
```
