```dataview
list WITHOUT ID tasks.text + " (" + link(file.link, Title) + ")"
flatten file.tasks as tasks
where contains(tasks.text, "[[" + this.file.name + "]]")
SORT tasks.text ASC
```

