---
description: List files a contact page is linked to as a contact log for this person
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
join(rows.file.link) AS "Contact note", 
rows.day + ": **" + min(rows.T) + " days**" AS "Last contact" 
FROM [[AB1908]] 
FLATTEN (date(today) - day).days AS T 
GROUP BY file.day
SORT min(rows.T) asc
```

### Only show the most recent contact

```dataview
TABLE WITHOUT ID 
join(rows.file.link) AS "Contact note", 
rows.day + ": **" + min(rows.T) + " days**" AS "Last contact" 
FROM [[AB1908]] 
FLATTEN (date(today) - day).days AS T 
GROUP BY file.day
SORT min(rows.T) asc
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