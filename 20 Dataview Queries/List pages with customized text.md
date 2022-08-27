---
description: Customize the output of a LIST query to fit your needs and to display more than one additional meta data value
topics:
  - 
---
#dv/list #dv/from 

# List pages and a custom output with them

## Basic 

```dataview
LIST "from " + author + " (Progress: " + pagesRead + "/" + totalPages + ")"
FROM #type/books 
```

## Variants

### Add formatting

```dataview
LIST WITHOUT ID "$" + price + " / **" + file.name + "** / " + genre + " / _" + publisher + "_"
FROM "10 Example Data/games"
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