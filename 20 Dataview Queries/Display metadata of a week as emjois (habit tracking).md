---
description: Display metadata of a certain week as emojis (i.e. for habit tracking)
topics:
  - habit tracking
  - emojis as output
---
#dv/table #dv/from  #dv/where #dv/choice
# Display metadata of a week as emjois (habit tracking)

## Basic 

```dataview
TABLE choice(praying, "💚", "➖") AS Praying, choice(breathing, "💚", "➖") AS breathing, choice(beingthankful, "💚", "➖") AS "being thankful", choice(slowdown, "💚", "➖") AS "slow down"
FROM "10 Example Data/dailys"
WHERE wellbeing.mood > 0 AND date(file.day).weekyear = 2
```

## Variants

Add the mood of the day as a smiley
```dataview
TABLE choice(wellbeing.mood = 1, "😢", choice(wellbeing.mood = 2 or wellbeing.mood = 3, "😐", choice(wellbeing.mood > 3, "😃", ""))) as Mood, choice(praying, "💚", "➖") AS Praying, choice(breathing, "💚", "➖") AS breating, choice(beingthankful, "💚", "➖") AS "being thankful", choice(slowdown, "💚", "➖") AS "slow down"
FROM "10 Example Data/dailys"
WHERE wellbeing.mood > 0 AND date(file.day).weekyear = 2
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
