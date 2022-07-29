---
description: Display values from a multivalue YAML frontmatter field
---
#dataviewquery
#dv/table #dv/from #dv/where 

# Multivalue YAML Frontmatter Field

## Basic 

```dataview
TABLE wellbeing.mood, wellbeing.mood-notes
FROM "10 Example Data/dailys"
WHERE wellbeing.mood = 4
```
