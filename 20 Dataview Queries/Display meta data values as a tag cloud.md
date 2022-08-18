---
description: Displays a set of values (i.e. from a meta data field) as a tag or word cloud
topics:
  - visualization
---
#dv/dataviewjs #dvjs/view


# Display meta data values as a tag cloud

## Basic 

> [!example] Sources of this query
> This query uses the [dv.view mechanism of dataview](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/#dvviewpath-input). This allows you to outsource dataview javascript code to a file in order to make it reusable. Additionally to that, it allows you to write css specific to this query. 
> You'll find the sources of this dv.view snippet under `00 Meta/dataview_views/tagcloud`. It expects the values you want to display as an array in the second argument.

```dataviewjs
await dv.view("00 Meta/dataview_views/tagcloud", 
	{
		values: dv.pages('"10 Example Data/dailys"').where(p => p.person).person
	})
```

> [!info] Usage in the dataview example vault
> This query is used to render the [[Topic Cloud]]!

> [!help]- Similar Queries
> Maybe these queries are of interest for you, too:
> ```dataview
> LIST
> FROM "20 Dataview Queries"
> FLATTEN topics as flattenedTopics
> WHERE contains(this.topics, flattenedTopics)
> AND file.name != this.file.name
> ```