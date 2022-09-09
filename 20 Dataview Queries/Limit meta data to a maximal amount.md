---
description: Limit not only result pages, but also their meta data values to a certain maximum
topics:
  - filter meta data
---

 #dv/TABLE #dv/FROM #dv/split #dv/join #dv/choice #dv/length #dv/list


> [!hint] Contributed by [via Discord](https://discord.com/channels/686053708261228577/1014259487445622855/1015226598141743104)

# Limit meta data to a maximal amount


## Basic 

> [!info] LIMIT data command
> If you want to limit your set of **result pages**, you can use `LIMIT` for this. See the [documentation](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#limit). This page concentrates on the question of how to limit meta data fields, i.e. outlinks, you get back for a page result. 

> [!warning] Need a unused character
> For the following code to work, you need to declare a UTF-8 character that is **not** used in your meta data value. Otherwise, you'll end up with broken data.

```dataview
TABLE split(join(file.outlinks, "�"),"�",3) As "Outlinks (first 3)"
FROM "30 Dataview Resources"
```

## Variants

### Only join and split if length is greater 3

This way you won't end up with empty bullet points in files with no outlinks

```dataview
TABLE choice(length(file.outlinks) <= 3, file.outlinks, split(join(file.outlinks, "�"),"�",3)) As "Outlinks (first 3)"
FROM "30 Dataview Resources"
```

### Do not rely on a unused character

For the method above to work, you need to settle down on a character that is absolutely not in use for the value you want to limit. Alternatively, you can use the following approach - this is safer, but gets more cumbersome if you want a high limit. 

```dataview
TABLE choice(length(file.outlinks) <= 3, file.outlinks, list(file.outlinks[0], file.outlinks[1], file.outlinks[2])) As "Outlinks (first 3)"
FROM "30 Dataview Resources"
LIMIT 5
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


