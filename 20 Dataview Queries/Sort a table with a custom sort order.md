---
description: Lets you define a custom sorting that is not alphabetical
topics:
  - custom sort
  - group pages based on meta data
---
#dv/table #dv/sort #dv/flatten #dv/where #dv/from  #dv/groupby #dv/default #dv/choice 


> [!hint] Contributed [via Discord](https://discord.com/channels/686053708261228577/875721010144477204/1006263776976318577)

# Sort a table with a custom sort order

## Basic 

```dataview
TABLE rows.file.link
FROM "10 Example Data/food"
WHERE recipe-type
GROUP BY recipe-type
SORT choice(recipe-type = "vegetarian", "1", choice(recipe-type = "meat", "2","3")) ASC
```

## Variants

### If you have a lot of values to sort

> [!info]- Query Explanation
> Wondering what's happening here? Let's have a look. First, we're calling `default(customsort, "99")` - that means "If the custom sort doesn't return anything, use 99 as the sort value" - and since we have less than 99 sort items, it'll put it to the very end (and sort all with the same value alphabetically).
> The magic happens here:
> ```
> ((x) => something)(G)
> ```
> We're calling `((x) => something)(G)`, meaning we define a [lambda](https://blacksmithgu.github.io/obsidian-dataview/query/expressions/#lambdas) function and put in G (our flattened Genre) as a parameter. G becomes x inside the function.
> ```
> { "Drama":1, 
> "Crime":2,
> "Horror": 3,
> "Comedy": 4,
> "Thriller": 5,
> "Science-Fiction": 6 }
> ```
> is an object that maps our genres to a numeric value that's in the end used to define the sorting. This is what puts "Drama" first and "Crime" second. By calling `[x]` at the very end, we "search" for the genre we pass into the lambda inside the function - returning its numeric value if available or nothing if we did not define it. In case of the latter, we'll get back `99` due to the `default` on top.

#### With a flattened field
```dataview
TABLE WITHOUT ID key AS "genre", rows.file.link AS "shows"
FROM "10 Example Data/shows"
FLATTEN Genre as G
GROUP BY G
SORT default(((x) => {
"Drama":1, 
"Crime":2,
"Horror": 3,
"Comedy": 4,
"Thriller": 5,
"Science-Fiction": 6
}[x])(G), "99") ASC
```

#### With no flattened field
```dataview
TABLE Show_status
FROM "10 Example Data/shows"
SORT default(((x) => {
"Running":1,
"To Be Determined": 2,
"Ended": 3
}[x])(show_status), "99") ASC
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