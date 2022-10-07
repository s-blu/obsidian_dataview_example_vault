---
description: Style columns of your table output without external css snippet and in DQL
topics:
  - custom output 
---
 #dv/TABLE #dv/FROM #dv/FLATTEN


> [!hint] Contributed by [mnvwvnm](https://discord.com/channels/686053708261228577/1014259487445622855/1027857346019459153)

# Style dataview table columns

## Basic 

```dataview
TABLE 
	publisher,
	developer,
    "<span style='display:flex; justify-content: right;'>" + price + "</span>" AS Price
FROM "10 Example Data/games"
```

## Variants

### Style multiple columns 

```dataview
TABLE styleStart + author + styleEnd AS Author, 
	genres, 
	styleStart + totalPages + styleEnd AS "Total Pages"
FROM "10 Example Data/books"
FLATTEN "<span style='font-weight: bold;'>" AS styleStart
FLATTEN "</span>" AS styleEnd
```

### Use different styles

```dataview
TABLE boldStyle + author + styleEnd AS Author, 
	genres, 
	rightAlignStyle + totalPages + styleEnd AS "Total Pages"
FROM "10 Example Data/books"
FLATTEN "<span style='font-weight: bold;'>" AS boldStyle
FLATTEN "<span style='display:flex; justify-content: right;'>" AS rightAlignStyle
FLATTEN "</span>" AS styleEnd
```

### Style page link

```dataview
TABLE WITHOUT ID styleStart + file.link + styleEnd AS "Book", 
	author,
	totalPages
FROM "10 Example Data/books"
FLATTEN "<span style='font-style: italic;'>" AS styleStart
FLATTEN "</span>" AS styleEnd
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
