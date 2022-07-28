---
description: Display metadata of a certain week as emojis (i.e. for habit tracking)
---

#querytype/table
#datacommand/FROM  #datacommand/WHERE 
#functions/choice 
# Display metadata of a week as emjois (habit tracking)

## Basic 

```dataview
TABLE choice(praying, "💚", "➖") AS Praying, choice(breathing, "💚", "➖") AS breating, choice(beingthankful, "💚", "➖") AS "being thankful", choice(slowdown, "💚", "➖") AS "slow down"
FROM "10 Example Data/dailys"
WHERE wellbeing.mood > 0 AND date(file.day).weekyear = 10
```

## Variants

Add the mood of the day as a smiley
```dataview
TABLE choice(wellbeing.mood = 1, "😢", choice(wellbeing.mood = 1 or wellbeing.mood = 2, "😐", choice(wellbeing.mood >= 3, "😃", ""))) as Mood, choice(praying, "💚", "➖") AS Praying, choice(breathing, "💚", "➖") AS breating, choice(beingthankful, "💚", "➖") AS "being thankful", choice(slowdown, "💚", "➖") AS "slow down"
FROM "10 Example Data/dailys"
WHERE wellbeing.mood > 0 AND date(file.day).weekyear = 10
```
