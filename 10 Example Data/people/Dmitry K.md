---
birthday: 1971-12-12
relationship: 
contacts: 
  phone: 780412712451
  mail: DmitryKri711212@aim.com
---

# Dmitry K

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

