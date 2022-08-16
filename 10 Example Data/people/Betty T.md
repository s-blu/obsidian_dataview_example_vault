---
birthday: 1984-07-31
relationship: 
contacts: 
  phone: 282908824961
  mail: bet672137@outlook.com
---

# Betty T

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

