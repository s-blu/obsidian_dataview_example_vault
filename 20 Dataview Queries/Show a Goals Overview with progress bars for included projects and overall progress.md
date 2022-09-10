---
description: Renders a table that allows overview about all projects that belong to a overarching goal as well as the total progress for this goal calculated from the projects' progress
topics:
  - progress tracking
  - progress bars
  - task tracking
---
#dv/dataviewjs #dvjs/tryQuery #dvjs/table 


> [!hint] Contributed by mnvwvnm

# Show a Goals Overview with progress bars for included projects and overall progress

## Basic 

```dataviewjs
const DQL = await dv.tryQuery(`
TABLE WITHOUT ID
	rows.file.link,
	map(rows, (r) => r.Lt),
	map(rows, (r) => r.Lc),
	map(rows, (r) => "<progress style='width:80px;' value='" + (r.Lc/r.Lt)*100 + "' max='100'></progress>" + "&nbsp;&nbsp;<span style='font-size:smaller;color:var(--text-muted)'>" + round((r.Lc/r.Lt)*100) + "%</span>")
FROM outgoing([[Goal 1]])
WHERE file.tasks
FLATTEN length(file.tasks) AS Lt
FLATTEN length(filter(file.tasks, (p) => p.completed)) AS Lc
GROUP BY true
`)

const globalValues = DQL.values
	.map(row =>  [
		removeBulletpoints(row[0]), // Project links
		removeBulletpoints(row[3]), // progress bars
		"<progress value='" + sumUp(row[2])/sumUp(row[1]) * 100 
		+ "' max='100'></progress><br><span style='font-size:smaller;'>" 
		+ Math.round(sumUp(row[2])/sumUp(row[1]) * 100) + "% completed</span>" 
	])

dv.table(["Projects", "Progress", "Goal Progress"], globalValues);


function removeBulletpoints(array) {
	return array.join("<br>")
}

function sumUp(val) {
	return val.reduce((acc, val) => acc + val, 0)
}
```

## Variants

### Show overall goal progress as last row

```dataviewjs
const DQL = await dv.tryQuery(`TABLE WITHOUT ID
	file.link,
	"<progress style='width:80px;' value='" + (Lc/Lt)*100 + "' max='100'></progress>" + "&nbsp;&nbsp;<span style='font-size:smaller;color:var(--text-muted)'>" + round((Lc/Lt)*100) + "%</span>"
FROM outgoing([[Goal 1]])
WHERE file.tasks
FLATTEN length(file.tasks) AS Lt
FLATTEN length(filter(file.tasks, (p) => p.completed)) AS Lc`)

const hrArray = Array(2).fill('<hr style="padding:0; margin:0 -10px; border-top: 1px solid var(--background-modifier-border)">');

const DQLglobal = await dv.tryQuery(`TABLE WITHOUT ID
	"Goal Progress",
	"<progress value='" + (sum(rows.Lc)/sum(rows.Lt))*100 + "' max='100'></progress>" + "&nbsp;&nbsp;<span style='font-size:smaller;'>" + round((sum(rows.Lc)/sum(rows.Lt))*100) + "%</span>"
FROM outgoing([[Goal 1]])
WHERE file.tasks
FLATTEN length(file.tasks) AS Lt
FLATTEN length(filter(file.tasks, (p) => p.completed)) AS Lc
GROUP BY true`)

DQL.values.push(hrArray)
DQL.values.push(DQLglobal.values.flatMap(r => r))

dv.table(["Projects", "Progress"], DQL.values);
```

### Show overview for all goals

```dataviewjs
const DQL = await dv.tryQuery(`
TABLE WITHOUT ID
	G AS Goals,
	rows.OUT,
	map(rows, (r) => r.Lt),
	map(rows, (r) => r.Lc),
	map(rows, (r) => "<progress style='width:80px;' value='" + (r.Lc/r.Lt)*100 + "' max='100'></progress>" + "&nbsp;&nbsp;<span style='font-size:smaller;color:var(--text-muted)'>" + round((r.Lc/r.Lt)*100) + "%</span>")
FROM #goal 
FLATTEN file.outlinks AS OUT
WHERE OUT.file.tasks
FLATTEN length(OUT.file.tasks) AS Lt
FLATTEN length(filter(OUT.file.tasks, (p) => p.completed)) AS Lc
GROUP BY file.link AS G
SORT G ASC
`)

const globalValues = DQL.values
	.map(row => {
	console.log(row)
	return [
		row[0], //Goals Link
		removeBulletpoints(row[1]), // Project links
		removeBulletpoints(row[4]), // progress bars
		"<progress value='" + sumUp(row[3])/sumUp(row[2]) * 100 
		+ "' max='100'></progress><br><span style='font-size:smaller;'>" 
		+ Math.round(sumUp(row[3])/sumUp(row[2]) * 100) + "% completed</span>" 
	]})

dv.table(["Goals", "Projects", "Progress", "Goal Progress"], globalValues);


function removeBulletpoints(array) {
	return array.join("<br>")
}

function sumUp(val) {
	return val.reduce((acc, val) => acc + val, 0)
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