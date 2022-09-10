---
description: Group a list of files according to their metadata
topics:
  - grouping
  - custom output
---
#dv/list #dv/from #dv/where #dv/groupby #dv/flatten #dv/join 

# Grouped list of files by their metadata
> [!tip] Tip
> After using a GROUP BY statement, results will be inside an object that looks like: 
> - {key: groupName; rows: ArrayOfDataColumns}
> 
>This means to refer to things in your TABLE/LIST after grouping, you should either use `key`, or `rows.fieldName` to access them.

## Basic 

List of files grouped by creation date:
```dataview
LIST rows.file.link
FROM "10 Example Data/books"
GROUP BY file.cday
```

## Variants

### Join grouped values into a string rather than a list
```dataview
LIST join(rows.file.link, " | ")
FROM "10 Example Data/books"
GROUP BY file.cday
```

### Create a custom field using Flatten
After grouping, it's usually only possible to display a single set of value under each group heading. In order to display something more complex, `FLATTEN` can be used to create a custom value that remains available after the `GROUP BY`. 

```dataview
LIST rows.customValue
FROM "10 Example Data/books"
FLATTEN file.link + " (" + author + ")" AS customValue
GROUP BY "**" + file.cday + "**"
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