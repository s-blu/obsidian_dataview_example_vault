---
birthday: 1987-09-18
relationship: accompanion
contacts: 
  phone: 734502259100
  mail: SophieBa_99@pm.com
---

# Sophie B

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

