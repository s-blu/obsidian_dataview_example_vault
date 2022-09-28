---
description: Showcase basic syntax of TABLE queries
topics:
  - basics
---
#dv/table #dv/from  #dv/where #dv/sort #dv/groupby  

# Basic Table Queries

## Basic 

**Show pages from a folder as table**
```dataview
TABLE
FROM "10 Example Data/games"
```

**Show pages from a tag  as table**
```dataview
TABLE
FROM #type/books 
```

**Combine multiple tags**
```dataview
TABLE
FROM #dvjs/el OR #dv/min 
```

**Combine multiple folders**
```dataview
TABLE
FROM "10 Example Data/books" OR "10 Example Data/games"
```

**Combine tags and folders**
```dataview
TABLE
FROM "10 Example Data/games" AND #genre/action  
```

**List all pages**

> [!attention] Add `dataview` to code block
> The output of this is pretty long. If you want to see it, add `dataview` to the code block - like on the examples above!
> Please note: There needs to be a **space** behind `TABLE` to see results!

```
TABLE 
```


## Variants

### Show pages from a certain author

```dataview
TABLE
FROM #type/books 
WHERE author = "Conrad C"
```

### Show pages and additional information

```dataview
TABLE author, pagesRead, totalPages
FROM #type/books
```

### Show only meta data information and no file link

```dataview
TABLE WITHOUT ID source, time, ingredients
FROM "10 Example Data/food"
WHERE source
```

### Group list elements

![[What is#^new-id-after-grouping]]

**Without additional columns**
```dataview
TABLE 
FROM "10 Example Data/books"
GROUP BY author
```

**With additional columns**
```dataview
TABLE rows.file.link, rows.pagesRead
FROM "10 Example Data/books"
GROUP BY author
```

### Customize table headers

**Of additional columns**
```dataview
TABLE contacts.phone AS "Phone Number", contacts.mail AS "E-Mail"
from "10 Example Data/people"
```

**Of the first (link/group) header without grouping**

```dataview
TABLE WITHOUT ID file.link AS "Game", developer, price
FROM "10 Example Data/games"
```

**Of the first (link/group) header with grouping**

```dataview
TABLE WITHOUT ID key AS "Author", rows.file.link AS "Books"
FROM "10 Example Data/books"
GROUP BY author
```

### Sort tables

```dataview
TABLE author
FROM "10 Example Data/books"
SORT author
```

> [!hint] Advanced usage
> Do you want to see more advanced examples? Head over to the [[Queries by Type#Table|Query Type Overview]] to see all available TABLE queries in the vault!

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
