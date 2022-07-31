---
description: Renders a progress bar for a percentage i.e. done tasks in file
---
#dv/inline #dv/dataviewjs #dv/table #dv/round #dv/from #dv/where 

# Render a progress bar

> [!info] Inline queries currently (v0.5.41) do not render in Live Preview mode. Switch to Read Mode to see the result.

pagesRead:: 42
totalPages:: 130

## Basic 

`$= const value = Math.round((dv.current().pagesRead / dv.current().totalPages) * 100); "<progress value='" + value + "' max='100'></progress>" + " " + value + "%"`

## Variants

### Calculate progress of task completion for current file

- [x] Task1
- [x] Task2
- [ ] Task3

`$= const value = Math.round(((dv.current().file.tasks.where(t => t.completed).length) / (dv.current().file.tasks).length || 0) * 100); "<progress value='" + value + "' max='100'></progress>" + " " + value + "%"`

### Rendering progress bar directly in tables or list 

This does not need a extra meta data field on the source files.

```dataview
TABLE pagesRead, totalPages, "<progress value='" + round(100*pagesRead/totalPages) + "' max='100'></progress> " + round(100*pagesRead/totalPages) + "%" AS Progress FROM "10 Example Data/books"
```


### Rendering custom styled progress bar directly in tables or list 
Thanks to Jillard and mnvwvnm!

```dataview
TABLE pagesRead, 
      totalPages, 
      "<div style='border-style:solid; border-width:1px; border-color:#AAAAAA;'><div align='center' style='background-color:"+ choice(per<50, "#d5763f", "#a8c373") +"; padding:5px; min-width:40px; width:" + per + "%;'>" + per + "%</div></div>" AS Progress
FROM "10 Example Data/books"
FLATTEN round(100*pagesRead/totalPages) AS per
```

### Rendering a progress bar that is stored inside a field on the source file

Also useable in tables, if put in an inline query on the source file.

> [!attention]
> For this to work, you need **avoid** using `dv.current()` in the source files. Using `dv.current()`, you would always see the progress of the _current_ file. Instead, give the explicit file, i.e. `dv.page("2022-01-03")` - have a look at the example data!

```dataview
TABLE task-completion
FROM "10 Example Data/dailys"
WHERE task-completion
```

```dataview
LIST task-completion
FROM "10 Example Data/dailys"
WHERE task-completion
```


