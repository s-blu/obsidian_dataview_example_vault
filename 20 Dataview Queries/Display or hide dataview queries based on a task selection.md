---
description: Hide or show dataview queries based on a task selection ("toggle tasks")
topics:
  - show or hide queries
---
#dv/dataviewjs #dvjs/current #dvjs/header #dvjs/list #dvjs/flatMap #dvjs/where 


> [!hint] Contributed by mnvwvnm

# Display or hide dataview queries based on a task selection

## Basic 

- [ ] Michel Foucault
- [x] Walter Benjamin
- [ ] Karl Marx

```dataviewjs
const checklist = dv.current().file.tasks.where(t => t.completed);

if (isActive("Michel Foucault")) {
    dv.header(2, "Michel Foucault quotes")
    dv.list(dv.pages('"10 Example Data/dailys"').flatMap(p => p.file.lists).where(l => l.author == "Michel Foucault").text)
}

if (isActive("Walter Benjamin")) {
    dv.header(2, "Walter Benjamin quotes")
    dv.list(dv.pages('"10 Example Data/dailys"').flatMap(p => p.file.lists).where(l => l.author == "Walter Benjamin").text)
}

if (isActive("Karl Marx")) {
    dv.header(2, "Karl Marx quotes")
    dv.list(dv.pages('"10 Example Data/dailys"').flatMap(p => p.file.lists).where(l => l.author == "Karl Marx").text)
}

function isActive(name) {
	return checklist.where(t => t.text == name)[0]
} 
```

## Variants

### Make code reusable, if the query to execute is always almost the same

If your dataview query only differs in the field value to select, like the example above, you can do a refactoring that makes it unnecessary to touch the code again when adding new authors.

> [!hint] When having "normal" tasks in the same file
> If you want to use "toggle tasks" along side normal tasks, the Basic approach is a bit safer. Nevertheless, you can use this one if you like, when you put your "toggle tasks" under a heading and filter for this, too, via `&& t.section.subpath === "Basic"` in the `where` function.
> If the only tasks in your file are "toggle tasks", you don't need this additional filter.

```dataviewjs
const checklist = dv.current().file.tasks.where(t => t.completed && t.section.subpath === "Basic");

checklist.forEach(task => showContent(task.text))

function isActive(name) {
	return checklist.where(t => t.text == name)[0]
} 

function showContent(author) {
	dv.header(2, author + " quotes")
    dv.list(dv.pages('"10 Example Data/dailys"').flatMap(p => p.file.lists).where(l => l.author == author).text)
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