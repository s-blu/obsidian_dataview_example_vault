---
description: Render a event-overview calendar when i.e. planning holidays
topics:
  - event planning
---
#dv/calendar #dv/where #dv/flatten #dv/list #dv/sort 

# Make a holiday planning with a bullet point list and the calendar view

## Basic 

> [!warning] Limitations
> The calendar is only for a rough overview and cannot display your events. The dot hover will always show you the whole page, instead of the concrete event happening.

- Some cool event [when:: 2022-08-14]
- Some cool event [when:: 2022-08-15]
- Some cool event happening later [when:: 2022-08-19]
- Some cool event happening later [when:: 2022-08-22]
- Some cool event [when:: 2022-08-18]
- Some cool event [when:: 2022-08-19]
- Some cool event [when:: 2022-08-19]
- Some cool event [when:: 2022-08-19]
- Second thing happening on 22th [when:: 2022-08-22]


```dataview
CALENDAR L.when
FROM "20 Dataview Queries/Make a holiday planning with a bullet point list and the calendar view"
FLATTEN file.lists AS L
WHERE L.when
```
It could be helpful to render a chronologically sorted List in addition:

```dataview
LIST WITHOUT ID L.text
FROM "20 Dataview Queries/Make a holiday planning with a bullet point list and the calendar view"
FLATTEN file.lists AS L
WHERE L.when
SORT L.when
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