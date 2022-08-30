---
description: Show all persons in your vault and when you had last contact with them 
topics:
  - contacts
  - latest items
---
#dv/table #dv/max #dv/from #dv/where #dv/flatten #dv/groupby #dv/sort #dv/min #dv/choice 


> [!hint] Contributed by mnvwvnm - Thanks!

# List the last contact with every person

## Basic 

```dataview
TABLE WITHOUT ID
contactedPerson AS "Person",
max(rows.file.day) AS "Last contact"
FROM "10 Example Data/dailys"
WHERE person
FLATTEN person AS contactedPerson
GROUP BY contactedPerson
SORT max(rows.file.day) DESC
```

## Variants

### Calculate elapsed days since last contact

```dataview
TABLE WITHOUT ID
contactedPerson AS "Person",
max(rows.file.link) AS "Last contact",
min(rows.elapsedDays) + " days" AS "Elapsed days"
FROM "10 Example Data/dailys"
WHERE person
FLATTEN (date(today) - file.day).days AS elapsedDays
FLATTEN person AS contactedPerson
GROUP BY contactedPerson
SORT max(rows.file.day) DESC
```

### Show a graphical representation how long the last contact has passed

```dataview
TABLE WITHOUT ID
contactedPerson AS "Person",
max(rows.file.link) AS "Last contact",
min(rows.elapsedDays) + " days" AS "Elapsed days",
choice(min(rows.elapsedDays)<30, "🟢", choice(min(rows.elapsedDays)<60, "🟡", choice(min(rows.elapsedDays)<90, "🟠", "☎️"))) AS "Return contact"
FROM "10 Example Data/dailys"
WHERE person
FLATTEN (date(today) - file.day).days AS elapsedDays
FLATTEN person AS contactedPerson
GROUP BY contactedPerson
SORT max(rows.file.day) DESC
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