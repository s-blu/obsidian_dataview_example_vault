---
description: Display values from a multivalue YAML frontmatter field
topics:
  - multivalue yaml
---
#dataviewquery
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