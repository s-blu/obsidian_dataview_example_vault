---
description: Show all bullet points that contain a certain tag
---
#dataviewquery
#dv/table #dv/from #dv/where #dv/groupby #dv/flatten #dv/contains 

# Show list items containing a certain tag

> [!todo] Create a new Query Note
> - [x] Use this template
> - [ ] Write a short description of the query in the Frontmatter
> - [ ] Write the most basic version of the query possible
> - [ ] If applicable, add one or multiple variants of the query and explain what they are doing
> - [ ] Add the appropiate querytype and all used datacommands and [functions](https://blacksmithgu.github.io/obsidian-dataview/query/functions/) to the frontmatter
> - [ ] Delete this callout :) 

## Basic 

```dataview
TABLE L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tag1")
```

## Variants
### grouping by file

```dataview
TABLE rows.L.text AS "My lists"
FROM "10 Example Data/dailys"
FLATTEN file.lists AS L
WHERE contains(L.tags, "#tag1")
GROUP BY file.link
```
