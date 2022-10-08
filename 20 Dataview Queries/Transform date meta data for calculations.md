---
description: Transform textual date informations in your meta data to proper dataview dates to do calculations with them
topics:
  - working with dates
---
 #dv/TABLE #dv/WHERE #dv/date #dv/replace #dv/FLATTEN #dv/regexreplace


# Transform date meta data for calculations

## Basic 

> [!hint] ISO format
> In order to be recognizable by dataviews `date` function, that again enables us to calculate with dates, the date needs to be in [ISO format](https://en.wikipedia.org/wiki/ISO_8601), in most cases something like `2022-10-08T19:03:22`. If your date is stored in another format, you need to transform it to fit ISO.

halfISO:: 2022-09-20 10:30

```dataview
TABLE halfISO, date(replace(halfISO, " ", "T"))
WHERE file = this.file
```

## Variants

### Calculate with dates after transformation

halfISO-start:: 2022-09-20 10:30
halfISO-end:: 2022-10-01 15:00

```dataview
TABLE start, end, end - start AS duration
WHERE file = this.file
FLATTEN date(replace(halfISO-start, " ", "T")) AS start
FLATTEN date(replace(halfISO-end, " ", "T")) AS end
```

### Using other formats

> [!info] Keep it as ISO as possible
> If your date format diverges a lot from the ISO format, transforming it becomes cumbersome and errorprone. For example, the following examples do not work if you have no time or do not use two-digits in the date. To keep yourself from trouble, whenever possible try to keep the ISO format as much as possible.

germanformat:: 22.09.2022 11:15

```dataview
TABLE date(regexreplace(germanformat, "([0-9]+).([0-9]+).([0-9]+) (.+)", "$3-$2-$1T$4")) AS "date"
WHERE germanformat
```

americanformat:: 09/25/2022 09:09 AM

```dataview
TABLE date(regexreplace(americanformat, "([0-9]+)/([0-9]+)/([0-9]+) ([0-9:]+)(.+)", "$3-$1-$2T$4")) AS "date"
WHERE germanformat
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
