# Table Query Examples

Query values from a multivalue yaml frontmatter field:
```dataview
TABLE wellbeing.mood, wellbeing.mood-notes
FROM "example_data/dailys"
WHERE wellbeing.mood = 4
```
---

Group days one felt "discomfort" after their pain intensity
```dataview
TABLE rows.file.link, rows.wellbeing.pain-type
FROM #daily 
WHERE wellbeing.mood-notes = "discomfort"
GROUP BY wellbeing.pain
```
---

Display set meta data as emoji from dailys of a specific week 
```dataview
TABLE wellbeing.mood as mood, choice(praying, "💚", "➖") AS Praying, choice(breathing, "💚", "➖") AS breating, choice(beingthankful, "💚", "➖") AS "being thankful", choice(slowdown, "💚", "➖") AS "slow down"
FROM "example_data/dailys"
WHERE wellbeing.mood > 0 AND date(file.day).weekyear = 10
```
