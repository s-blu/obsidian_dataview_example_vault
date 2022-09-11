---
description: Showcase basic syntax of TASK Queries
topics:
  - basics
---
 #dv/TASK #dv/FROM #dv/WHERE #dv/groupby #dv/contains #dv/SORT

# Basic Task Queries

## Basic 

> [!hint] Relationship between Tasks and Pages
> The `TASK` query type is special, because unlike all other query types (`LIST`, `TABLE`, `CALENDAR`) `TASK` does not operate on **page level** but on **task level**. If a page contains three tasks, you'll get back **three** results instead of one, like you'd get with any other query type. This allows us to filter for task specific properties, like included tags, meta data or text. Be aware though, that **every task inherits all properties from the page it's in**. Read more about [how task queries behave](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#task-queries) and [what for information you have available](https://blacksmithgu.github.io/obsidian-dataview/data-annotation/#tasks).

**List tasks  from a folder**
```dataview
TASK
FROM "10 Example Data/assignments"
```

**List tasks from a tag**
```dataview
TASK
FROM #next
```

**Combine multiple tags**
```dataview
TASK
FROM #clientC OR #clientB
```

**Combine multiple folders**
```dataview
TASK
FROM "10 Example Data/assignments" OR "10 Example Data/games"
```

**Combine tags and folders**
```dataview
TASK
FROM "10 Example Data/assignments" AND #later  
```

**List all tasks, everywhere**

> [!attention] Add `dataview` to code block
> The output of this is pretty long. If you want to see it, add `dataview` to the code block - like on the examples above!

```
TASK
```

## Variants

### List only open tasks

```dataview
TASK
FROM "10 Example Data/assignments"
WHERE !completed
```

### Group tasks by file

```dataview
TASK
FROM "10 Example Data/assignments"
GROUP BY file.link
```

### Show tasks that have a certain tag

```dataview
TASK
FROM "10 Example Data/assignments"
WHERE contains(tags, "#later")
```

### Show tasks with a due date (a task-located meta data field)

> [!info] Meta data on task level
> You can add meta data on tasks via the inline meta data syntax, i.e. `[duedate:: 2022-09-09]` - or `[contact:: Petro]`. Just be sure to wrap it into square brackets, so that data view can interpret it correctly. 

```dataview
TASK
FROM "10 Example Data/assignments"
WHERE duedate
```

### Sort task after completion date

> [!attention] Only possible with designated meta data
> A task does not know its completion date out of the box. In order to query for it, you need to add it to the task as an inline meta data field. Dataview provides an automatism for this: In the dataview options, at the very bottom, activate "Automatic Task Completion Date" to automatically append a completion date when checking a task.
> ![[Basic_Task_Queries_completion_screenshot.png|500]]
> ⚠ **Attention!** Dataview can only add this information **if you check a task inside a dataview output** - meaning inside a TASK Query!

```dataview
TASK
FROM "10 Example Data/assignments"
WHERE completed
SORT completion
```

> [!hint] Advanced usage
> Do you want to see more advanced examples? Head over to the [[Queries by Type#Task|Query Type Overview]] to see all available TASK queries in the vault!

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
