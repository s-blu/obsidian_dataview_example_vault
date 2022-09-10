---
description: Marks all days in a calendar where you spent more than a money limit (i.e. 75)
topics:
  - tresholds
---
#dv/table #dv/from #dv/flatten #dv/where #dv/round #dv/sum #dv/map #dv/number #dv/regexreplace 

# Mark all days in a calendar where you spent a certain amount of money

## Basic 

```dataview
CALENDAR file.mtime
FROM "20 Dataview Queries"
FLATTEN round(sum(paid)) as SUM
WHERE paid and SUM > 75
```

bought:: Nike shoes
paid:: 99

bought:: Delicious Cake
paid:: 7

## Variants

### When using expenses in form of "99 $"

^8d9d50

> [!info]
> You'll need to go back to Januray/Februrary 2022 to see the data

```dataview
CALENDAR file.day
FROM "10 Example Data/dailys"
FLATTEN round(sum(map(paid, (x) => number(regexreplace(x, " ?\$", ""))))) as SUM
WHERE paid and SUM > 75
```

> [!tip]
> When you try to write complex calendar queries, write a TABLE query first to make sure your query returns the results you're expecting.

```dataview
TABLE paid, SUM
FROM "10 Example Data/dailys"
FLATTEN round(sum(map(paid, (x) => number(regexreplace(x, "\$", ""))))) as SUM
WHERE paid and SUM > 75
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