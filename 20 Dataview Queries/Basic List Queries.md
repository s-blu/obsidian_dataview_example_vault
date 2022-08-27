---
description: Showcase basic syntax of LIST queries
topics:
  - basics
---
#dv/list #dv/from #dv/where 


> [!hint] Contributed by PutYourNameOrSourceHere

# Basic List Queries


## Basic 
**List pages from a folder**
```dataview
LIST
FROM "10 Example Data/games"
```

**List pages from a tag**
```dataview
LIST
FROM #type/books 
```

**Combine multiple tags**
```dataview
LIST
FROM #dvjs/el OR #dv/min 
```

**Combine multiple folders**
```dataview
LIST
FROM "10 Example Data/books" OR "10 Example Data/games"
```

**Combine tags and folders**
```dataview
LIST
FROM "10 Example Data/games" AND #genre/action  
```

**List all pages**

> [!attention] Add `dataview` to code block
> The output of this is pretty long. If you want to see it, add `dataview` to the code block - like on the examples above!

```
LIST
```

## Variants

### List pages from a certain author

```dataview
LIST
FROM #type/books 
WHERE author = "Conrad C"
```

### List pages and show a meta data field

For lists, you can only add **one** additional output. For more, you need to use a [[Basic Table Queries|table]] or [[List pages and a custom output with them|create a custom output]]

```dataview
LIST author
FROM #type/books
```

### List meta data values instead of the pages

i.e. list source links of your recipes:

```dataview
LIST WITHOUT ID source
FROM "10 Example Data/food"
WHERE source
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