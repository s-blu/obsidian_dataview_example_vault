---
description: Showcase the various possible usages of the FLATTEN data command
topics:
  - basics
nestedField:
  - value1
  - value2
  - value3
  - valueWithSubValues:
    - sub1
    - sub2
    - sub3
---
 #dv/TABLE #dv/FROM #dv/FLATTEN #dv/groupby #dv/WHERE #dv/meta #dv/contains #dv/round

# Example FLATTEN Queries

## Basic 

> [!info] Effect of FLATTEN
> `FLATTEN` is the opposite of `GROUP BY`. Instead of putting multiple notes into one row, it (potentionally) **splits up** one note into **multiple rows**. If your result contains seven notes and you use `FLATTEN` on a **multi value field**, you'll get `7 * sum of values in flattened field` results.
> [Documentation](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#flatten)


**Query without FLATTEN**
```dataview
TABLE genres
FROM "10 Example Data/books"
```

**Query with FLATTEN**
```dataview
TABLE genres
FROM "10 Example Data/books"
FLATTEN genres
```

> [!info] `FLATTEN` is a data command
> `FLATTEN` needs to be used in combination with a [[Learn the Basics#Understanding Query Types|Query Type]]. You can use `FLATTEN` multiple times. 

## Variants

### FLATTEN multiple fields

> [!info] You'll get `files * sum of values first field * sum of values second field * ...` results

```dataview
TABLE genres, booktopics
FROM "10 Example Data/books"
FLATTEN genres
FLATTEN booktopics
```

### Group by a flattened field

A popular use case for `FLATTEN` is to use a **multi value field for grouping**. Without flattening the multi value field first, the result is somewhat unexpected.

**Without flattening**
```dataview
TABLE rows.file.link
FROM "10 Example Data/books"
GROUP BY genres
```

**Grouping after flattening**

```dataview
TABLE rows.file.link
FROM "10 Example Data/books"
FLATTEN genres
GROUP BY genres
```

> [!attention] Order matters!
> Please mind that the **order is important** - a flattened field is only available _after_ you wrote the `FLATTEN` command. **One big exception**: The Query Type command is always **the last** command to be executed - despite standing at the very top! That means **all flattened fields are available as fields for your Query Type**.

If you **first group, then FLATTEN, you won't get the desired result!**
```dataview
TABLE rows.file.link
FROM "10 Example Data/books"
GROUP BY genres
FLATTEN genres
```

## Use FLATTEN to perform other operations on your values

> [!hint] Use function that cannot operate on lists
> To use functions that do not take an lists (a multi value) as an argument, you need to `FLATTEN` this value first. This is also true for functions that act differently on single values, i.e. `contains`

**Use a function that only takes single values as arguments**
```dataview
TABLE L.text
FROM "10 Example Data/dailys/2022-07-22"
FLATTEN file.lists AS L
WHERE meta(L.section).subpath = "Research"
```

**Use a function that operates differently on single values**
```dataview
TABLE L.text
FROM "10 Example Data/dailys/2022-07-22"
FLATTEN file.lists AS L
WHERE contains(L.text, "nul")
```


### Use FLATTEN to declare a new field

> [!hint] Flattening single values
> `FLATTEN` splits up multi value fields into single values, but it can also be performed on values that are already single value. Doing this, the number of your result rows won't change - so it wont `FLATTEN` in the traditional sense - but you're able to _name_ the flattened field and use it in your query (after the `FLATTEN` command and in your Query Type).
> This can be handy when you performing lengthy operations on fields and want to "save" the result of that instead of typing it over and over again.

```dataview
TABLE pagesRead, totalPages, progress
FROM "10 Example Data/books"
FLATTEN round((pagesRead / totalPages) * 100) + "%" AS progress
```

You can then do additional operations on your new, temporary field, too.

```dataview
TABLE pagesRead, totalPages, progress AS "%"
FROM "10 Example Data/books"
FLATTEN round((pagesRead / totalPages) * 100) AS progress
WHERE progress < 50
```

#### Use FLATTEN on a multi-value field but calculate a single value

> [!hint] Special case of declaring a new field
> There is one special case FLATTEN can act a bit unintuitive. When you 

```dataview
TABLE rows.file.link, rows.genreCount
FROM "10 Example Data/books"
FLATTEN length(genres) AS genreCount
GROUP BY genres
```

### Flattening a field multiple times

You can `FLATTEN` a field multiple times to change the value after other operations.

```dataview
TABLE pagesRead, totalPages, percentage
FROM "10 Example Data/books"
FLATTEN round((pagesRead / totalPages) * 100) AS progress
WHERE progress < 50
FLATTEN progress + "%" AS percentage
```

### About flattening nested fields

> [!error] FLATTEN on objects has no effect
> `FLATTEN` works only correctly on lists or single values. A nested field, like you see in the frontmatter of this file, _is_ a list, but `valueWithSubValues` is an object - and one element in the list you're flattening. Therefore, it'll appear as one row.

```dataview
TABLE nestedField
WHERE file = this.file
FLATTEN nestedField
```

The same is true for pure objects, they cannot be flattened. This `FLATTEN` **has no effect**.

```dataview
TABLE wellbeing
FROM "10 Example Data/dailys/2022-01-05"
FLATTEN wellbeing
```

> [!hint] More Examples
> Do you want to see more examples how `FLATTEN` can be used? Head over to [[Queries by Data Command#FLATTEN]] to see all queries in this vault that use `FLATTEN`.

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
