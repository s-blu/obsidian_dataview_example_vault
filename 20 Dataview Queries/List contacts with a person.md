---
description: List files a contact page is linked to as a contact log for this person
topics:
  - contacts
---
#dv/table #dv/from #dv/join #dv/min #dv/flatten #dv/groupby #dv/sort #dv/date #dv/limit #dv/contains 

> [!hint] Contributed by [mnvwvnm via Discord](https://discord.com/channels/686053708261228577/875721010144477204/1003820438696243260)


# List contacts with a person

## Basic 

> [!hint] Use on a contact page
> If you want to use this snippet on the contact page of the person directly, you can replace `FROM [[person]]` with `FROM [[]]`. See [[AB1908]] as an example. If you want to look at _all_ files, everywhere, skip the additional `"AND something"` in FROM.

```dataview
TABLE WITHOUT ID 
file.link AS "Contact note", 
day AS "Contact date"
FROM [[AB1908]] AND "10 Example Data/dailys"
```

## Variants

### Show days since last contact

```dataview
TABLE WITHOUT ID
file.link AS "Contact notes",
file.day + ": **" + T + " days**" AS "Last contacts" 
FROM [[AB1908]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
```

### Only show the most recent contact

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[AB1908]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

### List contacts to a person without a person page

If the person is a link to a nonexisting page:

```dataview
TABLE WITHOUT ID 
file.link AS "Contact note", 
day AS "Contact date"
FROM [[Paul]] AND "10 Example Data/dailys"
```

... or if the person is a textual metadata field:

```dataview
TABLE WITHOUT ID 
file.link AS "Contact note", 
day AS "Contact date"
FROM "10 Example Data/dailys"
WHERE contains(person, "Christa")
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