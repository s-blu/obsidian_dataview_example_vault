---
description: Displays a set of values (i.e. from a meta data field) as a tag or word cloud
topics:
  - visualization
---
#dv/dataviewjs #dvjs/view


# Display meta data values as a tag cloud

## Basic 

![[What is ...#^dv-view]]

> [!example] Sources
> You'll find the sources of this dv.view snippet under `00 Meta/dataview_views/tagcloud`. It expects the values you want to display as an array in the second argument.

```dataviewjs
await dv.view("00 Meta/dataview_views/tagcloud", 
	{
		values: dv.pages('"10 Example Data/dailys"').where(p => p.person).person
	})
```

> [!info] Usage in the dataview example vault
> This query is used to render the [[Topic Overview]]!

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
const inlinksFromUseCases = dv.current().file.inlinks.filter(link => link.path.contains("33 Use Cases"));

const header = `> [!info] Part of Use Cases`;

if (inlinksFromUseCases.length > 1) {
	const list = inlinksFromUseCases.array().reduce((acc, curr) => `${acc}</br> - ${curr}`,"")

	dv.span(`${header}
    > This query is part of following use cases:
    > ${list}
    > 
	`)
} else if (inlinksFromUseCases.length === 1) {
	dv.span(`${header}
    > This query is part of use case ${inlinksFromUseCases[0]}.
	`)
}
```