---
description: Add a meta data, i.e. the priority, as a color code in front of your tasks
topics:
  - task tracking
  - visualization
  - custom output 
---
 #dv/dataviewjs #dvjs/pages #dvjs/taskList 


> [!hint] Contributed by [mnvwvnm](https://discord.com/channels/686053708261228577/1014259487445622855/1027026939862597702)

# Colorcode tasks based on meta data


## Basic 

```dataviewjs
// define pages
const pages = dv.pages('"10 Example Data/projects"')

// OPEN TASKS
const tasks = pages.file.tasks.where(t => t.priority && !t.completed)

// priorities color
const red = "<span style='border-left: 3px solid red;'>&nbsp;</span>"
const orange = "<span style='border-left: 3px solid orange;'>&nbsp;</span>"
const green = "<span style='border-left: 3px solid rgb(55 166 155);'>&nbsp;</span>"

// regex to remove the field priority in text
const regex = /\[priority[^\]]+\]/g

// assign colors according to priority
for (let task of tasks){
	task.visual = "";
	
    if (task.priority === "high") {
        task.visual = red
    } else if (task.priority === "medium") {
        task.visual = orange
    } else if (task.priority === "low") {
        task.visual = green
    }
    task.visual += task.text.replace(regex, "");
}

// render open tasks sorted after priority
const order = [ "low", "medium", "high"]
dv.taskList(tasks.sort((a, b) => order.indexOf(b.priority) - order.indexOf(a.priority)), false)
```

## Variants

### Show newest completed tasks with low opacity

```dataviewjs
// define pages
const pages = dv.pages('"10 Example Data/projects"')

// OPEN TASKS
const tasks = pages.file.tasks.where(t => t.priority && !t.completed)

// priorities color
const red = "<span style='border-left: 3px solid red;'>&nbsp;</span>"
const orange = "<span style='border-left: 3px solid orange;'>&nbsp;</span>"
const green = "<span style='border-left: 3px solid rgb(55 166 155);'>&nbsp;</span>"

// regex to remove the field priority in text
const regex = /\[priority[^\]]+\]/g

// assign colors according to priority
for (let task of tasks){
	task.visual = "";
	
    if (task.priority === "high") {
        task.visual = red
    } else if (task.priority === "medium") {
        task.visual = orange
    } else if (task.priority === "low") {
        task.visual = green
    }
    task.visual += task.text.replace(regex, "");
}

// render open tasks
const order = [ "low", "medium", "high"]
dv.taskList(tasks.sort((a, b) => order.indexOf(b.priority) - order.indexOf(a.priority)), false)


// COMPLETED TASKS
const done = pages.file.tasks.where(t => t.priority && t.completed)

// render completed tasks and add a limit to the number of the listed tasks (sorted by the completion date - need to activate auto-completion in dataview settings)
if (done.length >= 1) {
    dv.taskList(done.sort(t => t.completion, 'desc').limit(10), false)
}

// change opacity of completed tasks
this.container.querySelectorAll("li.task-list-item.is-checked").forEach(s => s.style.opacity = "30%")
```

### In case of more priority values, use a map object

```dataviewjs
// define pages
const pages = dv.pages('"10 Example Data/projects"')

// OPEN TASKS
const tasks = pages.file.tasks.where(t => t.priority && !t.completed)

const priorityColorMap = {
	low: "rgb(55 166 155)",
	medium: "orange",
	high: "red",
}

// regex to remove the field priority in text
const regex = /\[priority[^\]]+\]/g

// assign colors according to priority
for (let task of tasks) {
	task.visual = getColorCode(task.priority) + task.text.replace(regex, "");
}

// render open tasks
const order = Object.keys(priorityColorMap)
dv.taskList(tasks.sort((a, b) => order.indexOf(b.priority) - order.indexOf(a.priority)), false)


// COMPLETED TASKS
const done = pages.file.tasks.where(t => t.completed)

// render completed tasks and add a limit to the number of the listed tasks (sorted by the completion date - need to activate auto-completion in dataview settings)
if (done.length >= 1) {
    dv.taskList(done.sort(t =>  t.priority &&  t.completion, 'desc').limit(10), false)
}

// change opacity of completed tasks
this.container.querySelectorAll("li.task-list-item.is-checked").forEach(s => s.style.opacity = "30%")

function getColorCode(priority) {
	const color = priorityColorMap[priority] ?? "grey";
	return `<span style='border-left: 3px solid ${color};'>&nbsp;</span>`
}
```

### Also show tasks that have no priority and sort them last

```dataviewjs
// define pages
const pages = dv.pages('"10 Example Data/projects"')

// OPEN TASKS
const tasks = pages.file.tasks.where(t => !t.completed)

const priorityColorMap = {
	low: "rgb(55 166 155)",
	medium: "orange",
	high: "red",
}

// regex to remove the field priority in text
const regex = /\[priority[^\]]+\]/g

// assign colors according to priority
for (let task of tasks) {
	task.visual = getColorCode(task.priority) + task.text.replace(regex, "");
}

// render open tasks
const order = Object.keys(priorityColorMap)
dv.taskList(tasks.sort((a, b) => order.indexOf(b.priority) - order.indexOf(a.priority)), false)


// COMPLETED TASKS
const done = pages.file.tasks.where(t => t.completed)

// render completed tasks and add a limit to the number of the listed tasks (sorted by the completion date - need to activate auto-completion in dataview settings)
if (done.length >= 1) {
    dv.taskList(done.sort(t => t.completion, 'desc').limit(10), false)
}

// change opacity of completed tasks
this.container.querySelectorAll("li.task-list-item.is-checked").forEach(s => s.style.opacity = "30%")

function getColorCode(priority) {
	const color = priorityColorMap[priority] ?? "grey";
	return `<span style='border-left: 3px solid ${color};'>&nbsp;</span>`
}
```

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
