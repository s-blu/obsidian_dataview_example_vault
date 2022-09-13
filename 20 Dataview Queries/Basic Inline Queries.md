---
description: Showcase basic syntax of DQL and JS Inline Queries
topics:
  - basics
multivalue:
  - val1
  - val2
  - val3
---
 #dv/inlinejs #dv/inline #dv/LIST #dv/WHERE

# Basic Inline Queries

## Basic 

### DQL

> [!info] Inline Queries: Use cases and Limitations
> Unlike a normal dataview block with three backticks, dataview inline queries are, like the name suggests, for the inline usage in text, headlines or similar to dynamically display values in the flow of your note instead of requiring a isolated block for them. 
> Inline Queries **always yield exactly one value**. Given that, it is not possible to perform page collecting operations with them - **Query types cannot be used inside Inline Queries**. Instead, they use [expressions](https://blacksmithgu.github.io/obsidian-dataview/query/expressions/).
> [Documentation](https://blacksmithgu.github.io/obsidian-dataview/data-queries/#inline-dql)

_This is an inline query - view in source mode to see the code:_ `= this.file.name`

### DataviewJS

> [!info] Dataview JS Inline Queries
> DataviewJS Inline Queries in the contrary have everything available that a `dataviewjs` block can use, making them immensively powerful. They need to be explicitly activated in the Dataviews Options.
> [Documentation](https://blacksmithgu.github.io/obsidian-dataview/data-queries/#inline-dataview-js)

_This is an inline query - view in source mode to see the code:_ `$= dv.current().file.name`

## Variants

### Showing file properties and meta data

Created: `= this.file.ctime`
Last Edited: `= this.file.mtime`
Description of the page: `= this.description`
Displaying a multi value field: `= this.multivalue` 

### Use dataview functions

> [!info] [Dataview functions](https://blacksmithgu.github.io/obsidian-dataview/query/functions/) are available in inline queries.

Lets better trim this description down to "`= truncate(this.description, 20, "...")`" - it's enough to see the start.

**Check if important meta data is set**
description: `= choice(contains(this, "description"), "Set", "Missing!")`
topics: `= choice(contains(this, "topics"), "Set", "Missing!")`
someOtherField: `= choice(contains(this, "someOtherField"), "Set", "Missing!")`

### Access meta data of other files

> [!info] 
> While you cannot write Queries in the traditional sense, you can still access concrete links and their properties.

The "`= [[Learn the Basics]].file.link`" Use Case exists since `= [[Learn the Basics]].file.ctime` and contains **`= length([[Learn the Basics]].file.outlinks)` outlinks** - `= choice(length(filter([[Learn the Basics]].file.outlinks, (x) => meta(x).path = this.file.path)), "including one to this file", "but none to this file")`.

### Formatting inline queries

> [!info] Inline Queries are treaten as text
> You can format an inline query like you'd format normal text.

Today is **`= date(today)`**, and it's **`= dateformat(date(now), "HH:MM")`**.

#### This file title is "`= this.file.name`"

_Last edited: `= this.file.mtime`_

### Using a inline query as a meta data value

> [!hint] Calculate a meta data field
> You can assign inline queries to a meta data field to use this calculation on other places, i.e. in a regular dataview query.

existsSince:: `= date(now) - this.file.ctime`

```dataview
LIST existsSince
WHERE existsSince
```

> [!hint] Inline DataviewJS
> With the help of Inline DataviewJS queries, you can even assign complete queries to a meta data field. This is a rather advanced technique, though.
> 

allAuthorsInVault:: `$= dv.pages('"10 Example Data/books"').groupBy(p => p.author).key`

```dataview
LIST allAuthorsInVault
WHERE allAuthorsInVault
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
