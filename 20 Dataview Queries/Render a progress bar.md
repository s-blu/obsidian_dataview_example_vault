---
description: Renders a progress bar for a percentage i.e. done tasks in file
topics:
  - progress tracking
  - visualization
  - progress bars
---
#dv/inline #dv/dataviewjs #dv/table #dv/round #dv/from #dv/where #dvjs/current

# Render a progress bar

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
TABLE pagesRead, totalPages, 

"<div style='border-style:solid; border-width:1px; border-color:#AAAAAA; display:flex;'>" + 
"<div align='center' style='padding:5px; min-width:10px; background-color:" +
	choice(percent < 50, "#d5763f", "#a8c373") + "; width:" +
	percent + "%; color:black'>" + 
choice(percent < 30, " </div><div style='padding:5px;'>", "") +
percent + "%</div></div>" AS Progress

FROM "10 Example Data/books"
FLATTEN round(100*pagesRead/totalPages) as percent
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

### Render a progress bar with additional textual information
Thanks to [Dovos!](https://discord.com/channels/686053708261228577/1014259487445622855/1018118073615650877)

**Over the complete vault for all tasks that contains "priority::"
`$= const valToSearch= "priority::"; const value = Math.round(((dv.pages().file.tasks.where(t => t.completed).where(t => t.text.includes(valToSearch)).length) / (dv.pages().file.tasks).where(t => t.text.includes(valToSearch)).length) * 100); "<progress value='" + value + "' max='100'></progress>" + "<span style='font-size:smaller;color:var(--text-muted)'> " + value + "% &nbsp;| &nbsp;" + (dv.pages().file.tasks.where(t => t.text.includes(valToSearch)).length - dv.pages().file.tasks.where(t => t.completed).where(t => t.text.includes(valToSearch)).length) + " left</span>"`

**All tasks of a specific file**
`$= const tasks = dv.page("10 Example Data/projects/project_9").file.tasks; const value = Math.round(tasks.where(t => t.completed).length / tasks.length * 100); "<progress value='" + value + "' max='100'></progress>" + "<span style='font-size:smaller;color:var(--text-muted)'> " + value + "% &nbsp;| &nbsp;" + (tasks.length - tasks.where(t => t.completed).length) + " left</span>"`

---
%% === end of query page === %%
> [!help]- Similar Queries
> Maybe these queries are of interest for you, too:
> ```dataview
> LIST
> FROM "20 Dataview Queries"
> FLATTEN topics as flattenedTopics
> WHERE contains(this.topics, flattenedTopics)
> AND file.name != this.file.name
> ```

```dataviewjs
dv.view('00 Meta/dataview_views/usedInAUseCase',  { current: dv.current() })
```