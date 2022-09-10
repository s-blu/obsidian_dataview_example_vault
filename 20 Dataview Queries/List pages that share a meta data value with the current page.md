---
description: List pages that have the same value in a field than the current one, i.e. to find recipes that share ingredients
topics:
  - navigation
  - group pages based on meta data
ingredients:
  - parsley
  - bacon
recipe-type: vegetarian
---
#dv/table #dv/from #dv/where #dv/flatten #dv/contains #dv/groupby #dv/length #dv/sort 


> [!hint] Contributed [via Discord](https://discord.com/channels/686053708261228577/875721010144477204/1006083409631789086)

# List pages that share a meta data value with the current page

## Basic 
**If you have a single value**:

```dataview
LIST
FROM "10 Example Data/food"
WHERE recipe-type = this.recipe-type
```

**If you have a multi value field (list)**:

```dataview
TABLE ings AS "shared ingredient"
FROM "10 Example Data/food"
WHERE ingredients
FLATTEN ingredients as ings
WHERE contains(this.ingredients, ings) AND file.name != this.file.name
```

## Variants

### Show file only once as result

```dataview
TABLE rows.ings AS "shared ingredient"
FROM "10 Example Data/food"
WHERE ingredients
FLATTEN ingredients as ings
WHERE contains(this.ingredients, ings) AND file.name != this.file.name
GROUP BY file.link
```

### Group by ingredient instead of file/recipe

```dataview
TABLE WITHOUT ID ings AS "shared ingredient", rows.file.link AS "recipes"
FROM "10 Example Data/food"
WHERE ingredients
FLATTEN ingredients as ings
WHERE contains(this.ingredients, ings) AND file.name != this.file.name
GROUP BY ings
```

### Calculate count of meta data value matches

```dataview
TABLE WITHOUT ID ings AS "shared ingredient", count AS "recipe count", rows.file.link AS "recipes"
FROM "10 Example Data/food"
WHERE ingredients
FLATTEN ingredients as ings
WHERE contains(this.ingredients, ings) AND file.name != this.file.name
GROUP BY ings
FLATTEN length(rows.file.link) as count
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