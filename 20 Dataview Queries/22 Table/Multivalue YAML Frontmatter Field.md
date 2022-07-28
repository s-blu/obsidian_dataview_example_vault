---
description: Display values from a multivalue YAML frontmatter field
---

#querytype/table
#datacommand/FROM  #datacommand/WHERE
# Multivalue YAML Frontmatter Field

## Basic 

```dataview
TABLE wellbeing.mood, wellbeing.mood-notes
FROM "10 Example Data/dailys"
WHERE wellbeing.mood = 4
```
