---
description: Display values from a multivalue YAML frontmatter field
topics:
  - multivalue yaml
---
#dv/table #dv/from #dv/where 

# Multivalue YAML Frontmatter Field

## Basic 

```dataview
TABLE wellbeing.mood, wellbeing.mood-notes
FROM "10 Example Data/dailys"
WHERE wellbeing.health > 2
```

## Variants

Add better readable table headers

```dataview
TABLE wellbeing.mood AS "Mood", wellbeing.mood-notes AS "Mood Notes"
FROM "10 Example Data/dailys"
WHERE wellbeing.health > 2
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