---
description: List all persons that have birthday the current month
topics:
  - contacts
  - date based overviews
---
#dv/list #dv/where #dv/from #dv/inline #dvjs/pages #dvjs/where 


> [!hint] Contributed [via Discord](https://discord.com/channels/686053708261228577/875721010144477204/1008491525321265232)

# Show all birthdays for this month

## Basic 

```dataview
LIST birthday
FROM "10 Example Data/people"
WHERE birthday.month = date(today).month
```

## Variants

### As inline query

`$=dv.pages('"10 Example Data/people"').where(p => p.birthday).where(p => p.birthday.month == dv.date('today').month).file.link`

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