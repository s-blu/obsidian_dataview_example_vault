---
birthday: 1972-03-25
relationship: 
contacts: 
  phone: 440029051936
  mail: OssQQ@outlook.com
---

# Osama W

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

