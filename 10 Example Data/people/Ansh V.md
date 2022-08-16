---
birthday: 1995-08-08
relationship: friend
contacts: 
  phone: 291677999336
  mail: Ansh_Vili13@icloud.com
---

# Ansh V

```dataview
TABLE WITHOUT ID
file.link AS "Contact note",
file.day + ": **" + T + " days**" AS "Last contact" 
FROM [[]] 
FLATTEN (date(today) - file.day).days AS T 
SORT file.day desc
LIMIT 1
```

