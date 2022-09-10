---
description: Group meta data fields after their order in a file (useful if you have multiples in the same file)
topics:
  - meta data grouping
---
#dv/dataviewjs #dvjs/pages #dvjs/where #dvjs/sort #dvjs/table 

# Group duplicated meta data fields after their order in file

## Basic 

```dataviewjs
const pages = dv.pages('"10 Example Data/dailys"').where(p => p.bought).sort(p => p.file.name)

const groupedValues = [];
for (let page of pages) {
	const length = Array.isArray(page.bought) ? page.bought.length : 1;
	for (let i = 0; i < length; i++) {
		groupedValues.push([
			page.file.link,
			getValue(page, "bought", i), 
			getValue(page, "paid", i)
		])
	}
}

dv.table(["Page", "Bought", "Paid"], groupedValues)

function getValue(page, key, i) {
	return page[key] && Array.isArray(page[key]) ? page[key][i] : page[key]; 
}
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