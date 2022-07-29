---
description: Display Files grouped after metadata where one felt discomfort
---

#querytype/table
#datacommand/FROM  #datacommand/WHERE #datacommand/GROUPBY 
#functions/choice
# Group files by meta data

## Basic 

```dataview
TABLE rows.file.link, rows.wellbeing.pain-type
FROM #daily 
WHERE wellbeing.mood-notes = "discomfort"
GROUP BY wellbeing.pain
```
## Variants

Add better readable table headers

```dataview
TABLE WITHOUT ID row.key AS "Pain", rows.file.link AS "Dailys", rows.wellbeing.pain-type AS "Type of Pain"
FROM #daily 
WHERE wellbeing.mood-notes = "discomfort"
GROUP BY wellbeing.pain
```

---

Replace pain numbers with textual information

```dataview
TABLE WITHOUT ID choice(row.key = 0, "None", choice(row.key = 1, "Little", choice(row.key = 2, "Middle", choice(row.key = 3, "High", row.key))))  AS "Pain", rows.file.link AS "Dailys", rows.wellbeing.pain-type AS "Type of Pain"
FROM #daily 
WHERE wellbeing.mood-notes = "discomfort"
GROUP BY wellbeing.pain
```