---
description: List the most recent contact with a certain person, or the most recent day you baked banana cake, or made a certain type of sports, for example. 
topics:
  - latest items
---
#dv/list #dv/from #dv/where #dv/sort #dv/limit #dv/inline #dvjs/pages #dvjs/where #dvjs/sort #dvjs/limit #dvjs/flatMap #dvjs/array #dvjs/last #dvjs/span


> [!hint] Contributed [via Discord](https://discord.com/channels/686053708261228577/875721010144477204/1007282419688284322)

# List most recent meta data value that contains a certain phrase

## Basic 

```dataview
LIST met
FROM "10 Example Data/dailys"
WHERE contains(met, "Sophie")
SORT file.name DESC
LIMIT 1
```

## Variants

### As an javascript inline field

> [!hint] Usage
> A inline query can be i.e. used as a field for the Kanban Board Plugin

`$=const notes = dv.pages('"10 Example Data/dailys"').where(p => p.met).where(p => String(p.met).includes("Sophie")).sort((p) => p.file.name, 'desc').limit(1); if (notes.length) { const content = notes.flatMap(m => dv.array(m.met)).where(m => m.includes("Sophie")).last(); dv.span(notes[0].file.link + ": " + content); }`

When editing this, it can be helpful to put it into a regular dataviewjs block while editing for better readability:

```dataviewjs
const notes = dv.pages('"10 Example Data/dailys"')
	.where(p => p.met)
	.where(p => String(p.met)
	.includes("Sophie"))
	.sort((p) => p.file.name, 'desc')
	.limit(1); 
	
if (notes.length) { 
	const content = notes
		.flatMap(m => dv.array(m.met)).where(m => m.includes("Sophie"))
		.last(); 
	
	dv.span(notes[0].file.link + ": " + content); 
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