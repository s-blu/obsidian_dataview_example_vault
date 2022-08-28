---
birthday: 2002-02-21
relationship: work-related
contacts: 
  phone: 853275063842
  mail: Markus_H@aim.com
---

# Markus H

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

