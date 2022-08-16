---
birthday: 1999-04-18
relationship: 
contacts: 
  phone: 264647459304
  mail: BehaBuhaBoba@outlook.com
---

# Behati L

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

