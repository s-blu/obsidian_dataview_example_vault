---
description: Customize the output of a LIST query to fit your needs and to display more than one additional meta data value
topics:
  - basics
  - custom output
---
#dv/list #dv/from 

# How to create custom outputs in queries

> [!hint] String concatenation
> You can create custom outputs with something called **string concatenation**. Basically, that means that you are adding strings - texts - and meta data together to one output, just like numbers.
> How you do this looks always the same, for example:
> `"Hello! This is file " + file.name`
> The part in `""` is a text, where you can type anything you want. Then, with a `+`, you can add to this text a meta data value, so it gets "summed up" and displayed as one value.
> You can add as many texts and variables as you want. See the examples below!

## Basic 

```dataview
LIST "from " + author 
FROM #type/books 
```

**With more elements**

```dataview
LIST "from " + author + " (Progress: " + pagesRead + "/" + totalPages + " pages)"
FROM #type/books 
```
## Variants

### Add formatting

```dataview
LIST WITHOUT ID "$" + price + " / **" + file.name + "** / " + genre + " / _" + publisher + "_"
FROM "10 Example Data/games"
```

### Usage in tables

```dataview
TABLE "Call under: " + contacts.phone AS "Phone" 
from "10 Example Data/people"
```

### Add HTML formatting

```dataview
TABLE contacts.phone + "<br>" + contacts.mail AS "Contacts", "<span style='color:red'>" + relationship + "</span>" AS "Relationship"
from "10 Example Data/people"
WHERE relationship
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