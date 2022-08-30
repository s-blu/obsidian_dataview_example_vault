---
description: Get the latest, not completed tasks 
topics:
  - open tasks
  - latest items
---
#dataviewquery
#dv/task #dv/from #dv/where #dv/sort #dv/limit 

# Get latest open tasks

> [!info] Difference between status and completed
> A task only counts as completed if its status is equals to "x". If you use custom task statuses, i.e. "-", a task will appear checked but is _not_ completed.

## Basic 

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE !completed
SORT file.day DESC
LIMIT 10
```

## Variants

If using custom statuses for TASKS, it's maybe better to check for `status = " "` instead of `!completed`, depending on your use case 

```dataview
TASK
FROM "10 Example Data/dailys"
WHERE status = " "
SORT file.day DESC
LIMIT 10
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