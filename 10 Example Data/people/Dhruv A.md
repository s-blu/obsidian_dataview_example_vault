---
birthday: 1972-01-17
relationship: friend
contacts: 
  phone: 210203461942
  mail: dhrrruvvv@yahoo.com
---

# Dhruv A

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

