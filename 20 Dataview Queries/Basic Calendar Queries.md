---
description: Showcase basic usage of Calendar Queries
topics:
  - basics
---
 #dv/CALENDAR #dv/FROM #dv/WHERE

# Basic Calendar Queries

> [!attention] Errornous Pagepreview as of v0.5.43
> When hovering over a dot, you get a page preview of this note. But beware: You'll see the same preview for all pages. 

## Basic 

> [!info] Usage of Calendar Query Type
> The Calendar Query Type needs a **valid date information** as a field in order to display notes. You always need to give this information. If the calendar query encounters a file you've queried that does not have your defined "date source" - or if it's invalid - the Calendar won't render at all.

> [!hint] You need to go to August 2022 or Jan/Feb 2022 to see results

**Query from a folder**
```dataview
CALENDAR file.day
FROM "10 Example Data/dailys"
```
**Query from a tag**
```dataview
CALENDAR file.day
FROM #daily 
```

**Query from a tag/folder combination**
```dataview
CALENDAR file.day
FROM "10 Example Data/dailys" OR #journal 
```

**Query for all pages, everywhere**

> [!hint] Query for "all"
> Unlike other Query Types, Calendar **always** need the datefield information. The most minimalistic Query for a Calendar looks like `CALENDAR <datefield>` - but then _all_ of your files need to have a valid date inside this specific field! 

```dataview
CALENDAR file.ctime 
```

## Variants

### Make sure the date information is available

```dataview
CALENDAR due
FROM "10 Example Data/assignments"
WHERE due
```

> [!hint] Advanced usage
> Do you want to see more advanced examples? Head over to the [[Queries by Type#Calendar|Query Type Overview]] to see all available CALENDAR queries in the vault!

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
