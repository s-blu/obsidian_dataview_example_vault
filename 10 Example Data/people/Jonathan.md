---
birthday: 1994-10-02
relationship: accompanion
contacts: 
  phone: 01796628361
  mail: 
---

# Jonathan

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

