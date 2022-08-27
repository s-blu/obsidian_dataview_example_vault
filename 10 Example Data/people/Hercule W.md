---
birthday: 1986-11-30
relationship: 
contacts: 
  phone: 869869919842
  mail: Hercule-W@hotmail.com
---

# Hercule W

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

