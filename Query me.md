
# Test File to reproduce #1553

Every file contains the Task count given in the folder name and **2 tasks** matching the query (linking to this file).

## Files without FLATTEN

ca. 0,5 sek
```
LIST
FROM "10 Example Data/todos/100files-a-10-todos"
```

ca. 5 sek
```
LIST metadatafield
FROM "10 Example Data/todos/1000files-a-10-todos"
```

ca. 0,1 sek
```
LIST metadatafield
FROM "10 Example Data/todos/10files-a-100-todos"
```

ca. 0,5 sek
```
LIST metadatafield
FROM "10 Example Data/todos/100files-a-100-todos"
```

ca. instant
```
LIST metadatafield
FROM "10 Example Data/todos/bad-files"
```

## Files with FLATTEN

ca. 1sek
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/100files-a-10-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

ca. 5 sek
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/1000files-a-10-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

ca. 1,5 sek
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/10files-a-100-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

ca. 17 sek
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/100files-a-100-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

**crashes** - around 2180 tasks in total, ca. 1500 matches the query. 
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/bad-files"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```