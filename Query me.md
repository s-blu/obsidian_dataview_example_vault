
# Test File to reproduce #1553

Every file contains the Task count given in the folder name and **2 tasks** matching the query (linking to this file).

## Files without FLATTEN

ca. 0,5 sec
```
LIST
FROM "10 Example Data/todos/100files-a-10-todos"
```

ca. 5 sec
```
LIST metadatafield
FROM "10 Example Data/todos/1000files-a-10-todos"
```

ca. 0,1 sec
```
LIST metadatafield
FROM "10 Example Data/todos/10files-a-100-todos"
```

ca. 0,5 sec
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

ca. 1 sec
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/100files-a-10-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

ca. 5 sec
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/1000files-a-10-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

ca. 1,5 sec
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/10files-a-100-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

ca. 17 sec
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/100files-a-100-todos"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

ca. 5 sec
```dataview
list tex + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/1500files-a-1-todos"
FLATTEN file.tasks.text AS tex
```

ca. 7 sec
```dataview
list tex + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/750files-a-2-todos"
FLATTEN file.tasks.text AS tex
```

ca. 20 sec, blocks input
```dataview
list tex + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/5files-a-300-todos"
FLATTEN file.tasks.text AS tex
```

**crashes** - around 2180 tasks in total, ca. 1500 matches the query. 
```
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
FROM "10 Example Data/todos/bad-files"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

