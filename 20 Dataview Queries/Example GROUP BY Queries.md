---
description: Showcase the various possible usages of the GROUP BY data command
topics:
  - basics
---
 #dv/LIST #dv/FROM #dv/groupby #dv/TABLE #dv/FLATTEN #dv/choice #dv/date #dv/WHERE #dv/round #dv/length

# Example GROUP BY Queries

## Basic 

> [!info] Effect of `GROUP BY`
> Initially, a dataview results yields the pages you receive from your `FROM` and `WHERE` arguments as results - one "row", one result item, per note. When a `GROUP BY` is applied to a Query, you **bundle up** all pages after the **field you're grouping by**. This has two implications:
> First, after a `GROUP BY`, you have as many results as the field you grouped by has values.
> Secondly, the result pages are not your "first level" anymore, but the group is. When listing out a grouped query, you will not receive the files anymore, but the groups. 
> [Documentation](https://blacksmithgu.github.io/obsidian-dataview/query/literals/)

```dataview
LIST
FROM "10 Example Data/books"
GROUP BY author
```

> [!hint] Working with grouped pages
> A grouped result list is made up of result items that look like this:
> `Key`: Value of the field you used in GROUP BY
> `rows`: All pages that match `Key`
> Before grouping, every note was a result item and file.link was the `Key`. After grouping, your file informations are bundled up under the group value as key under the field `rows`. That means you need to use `rows` as a prefix when listing informations.

```dataview
TABLE rows.file.link
FROM "10 Example Data/books"
GROUP BY author
```


## Variants

### When pages match multiple groups

> [!info] Duplication of entries
> If a page matches multiple groups, dataview will duplicate the page for you to put it in every matching group. Therefor, pages can show up multiple times in a grouped result list.

> [!question] Why do we need to use `FLATTEN` here first?
> In order to get decent groups, we need to `FLATTEN` the multi value field `genres` first. Read more about that in [[Example FLATTEN Queries#Group by a flattened field]]

```dataview
TABLE rows.file.link
FROM "10 Example Data/books"
FLATTEN genres
GROUP BY genres
```

### Use a calculation as a group

> [!info]
> It's also possible to use a calculation as a group, not only a plain field. 

```dataview
LIST rows.file.link
FROM "10 Example Data/assignments"
GROUP BY choice(due < date(today), "Overdue", "Still has time")
```

In addition, you can name this calculation to reference it further in your query.

```dataview
TABLE WITHOUT ID progress + "%" AS "% read", rows.file.link
FROM "10 Example Data/books"
GROUP BY round((pagesRead/totalPages) * 100) as progress
WHERE progress > 50 AND progress < 100
```
### Group by literals to trim down your result to exactly one result

> [!info]
> Beside calculations and fields, you can use a [literal](https://blacksmithgu.github.io/obsidian-dataview/query/literals/) - a fixed value - as a group. This will always result into **one group** and can be useful in certain scenarios, i.e. if you want to calculate a sum or average of your data.
> The literal itself is used as the group name, but doesn't matter otherwise. You can use it to declare a senseful prefix or omit it completely by using `WITHOUT ID`.

```dataview
LIST length(rows) 
FROM "10 Example Data/books"
GROUP BY "Total Books in Obsidian"
```

> [!hint] More Examples
> Do you want to see more examples how `GROUP BY` can be used? Head over to [[Queries by Data Command#GROUPBY]] to see all queries in this vault that use `GROUP BY`.

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
