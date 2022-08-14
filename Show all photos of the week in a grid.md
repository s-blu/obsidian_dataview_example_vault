---
description: %% What does the query do? %%
---
#dv/


> [!hint] Contributed by PutYourNameOrSourceHere

# Show all photos of the week in a grid

> [!todo] Create a new Query Note
> - [x] Use this template
> - [ ] Write a short description of the query in the frontmatter
> - [ ] Write the most basic version of the query possible. Keeping it simple and reduce it to the necessary makes it easier for others to understand the important parts of a query
> - [ ] If applicable, add one or multiple variants of the query and explain what they are doing - this could i.e. be an enhancement that makes the result better readable/even more useful
> - [ ] Add appropiate tags to the page 
> 	- [ ] If a DQL query: used query type (LIST, TABLE etc), data commands (FROM, WHERE, FLATTEN etc) and used [functions](https://blacksmithgu.github.io/obsidian-dataview/query/functions/) - always with #dv in front, i.e. #dv/list 
> 	- [ ] If a dataviewjs query: #dv/dataviewjs  and every [dataviewjs](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/) or [data array](https://blacksmithgu.github.io/obsidian-dataview/api/data-array/) function as a #dvjs tag, i.e. #dvjs/current 
> - [ ] Add your name in the contribution callout at the top - or remove the contribution callout, however you like it better! Mind, though: Before contributing queries from others, always ask for their permission.
> - [ ] Delete this callout :) 

## Basic 

> [!attention] Additional CSS Snippet required
> A CSS Snippet is in place to style this query. You'll find it [here](.obsidian\snippets\show-photos-of-the-week-as-grid.css)

> [!info] Usage in a weekly note
> When you want to use this query in a weekly note and your weekly note is named like "2022W02", use this as the first line: `const yearAndWeek = dv.current().file.name.split('-W')`. This will retrieve the year and weeknumber information from your file name and you do not need to adjust this manually.

```dataviewjs
const yearAndWeek = ["2022", "02"]
const pages = dv.pages('"10 Example Data/dailys"').where(p => p.day && p.day.year == yearAndWeek[0] && p.day.weekNumber == yearAndWeek[1])
dv.container.className += ' imagegrid'
dv.list(pages.picoftheday)
```

## Variants

### Use as view snippet with a library for a nice layout

```dataviewjs
await dv.view('00 Meta/dataview_views/imagegrid')

```