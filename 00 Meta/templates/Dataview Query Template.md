---
description: %% What does the query do? %%
topics:
  - 
---
#dv/


> [!hint] Contributed by PutYourNameOrSourceHere

# {{title}}

> [!todo] Create a new Query Note
> - [x] Use this template
> - [ ] Write a short description of the query in the frontmatter
> - [ ] Write the most basic version of the query possible. Keeping it simple and reduce it to the necessary makes it easier for others to understand the important parts of a query
> - [ ] If applicable, add one or multiple variants of the query and explain what they are doing - this could i.e. be an enhancement that makes the result better readable/even more useful
> - [ ] Add appropriate tags to the page 
> 	_Hint: Adding queries often? Consider using the [[Templater Tag Auto Generation]]_
> 	- [ ] If a DQL query: used query type (LIST, TABLE etc), data commands (FROM, WHERE, FLATTEN etc) and used [functions](https://blacksmithgu.github.io/obsidian-dataview/query/functions/) - always with #dv in front, i.e. #dv/list 
> 	- [ ] If a dataviewjs query: #dv/dataviewjs and every [dataviewjs](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/) or [data array](https://blacksmithgu.github.io/obsidian-dataview/api/data-array/) function as a #dvjs tag, i.e. #dvjs/current 
> - [ ] Add topics to the frontmatter that helps the query at the end of the page to list similar queries. Head over to the [[Topic Overview]] to see what's available and be welcome to introduce new topics where appropriate!
> - [ ] Add your name in the contribution callout at the top - or remove the contribution callout, however you like it better! Mind, though: Before contributing queries from others, always ask for their permission.
> - [ ] Delete this callout :) 

## Basic 

```dataview

```

## Variants

### Description of Variant A - what does it differently? What do we achieve with that?

```dataview

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
