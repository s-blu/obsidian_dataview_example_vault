---
description: Show a sum row for numeric values and durations
topics:
  - sums
---
#dv/dataviewjs  #dvjs/tryQuery #dvjs/table 

# Show a sum row for a numeric table

## Basic

```dataviewjs
// Paste your DQL for the table here:
const query = `TABLE situps, steps
FROM "10 Example Data/dailys"
WHERE file.day.month = 2`
// change the name of the total row, if you like:
const nameOfTotalRow = "Sums";


// you don't need to touch this, normally.
// get the data from the query above
let DQL = await dv.tryQuery(query);
const sums = [nameOfTotalRow];
// for each header (except the first one, which is "File")...
for (let i = 1; i < DQL.headers.length; i++) {
	let sum = 0;
	// ... and for each row ...
	for (let k = 0; k < DQL.values.length; k++) {
		// get the current cell (row k and column i) and add it to the sum, if set
		let currentValue = DQL.values[k][i];
		if (currentValue) sum += currentValue 
	}
	if (!sum) sum = ""
	sums.push(sum);
}
// add a divider line for visual distinction between the query and the sums (thanks, Jillard!), add both to the table data
let hrArray = Array(DQL.headers.length).fill('<hr style="padding:0; margin:0 -10px;">');
DQL.values.push(hrArray)
DQL.values.push(sums)
//print the table
dv.table(DQL.headers, DQL.values)
```

## Variants

Be able to calculate Durations and ignore non numeric or duration values

```dataviewjs
// Paste your DQL for the table here:
const query = `TABLE praying, training, situps, steps
FROM "10 Example Data/dailys"
WHERE file.day.month = 2`
// change the name of the total row, if you like:
const nameOfTotalRow = "Sums";


// you don't need to touch this, normally.
// get the data from the query above
let DQL = await dv.tryQuery(query);
const sums = [nameOfTotalRow];
// for each header (except the first one, which is "File")...
for (let i = 1; i < DQL.headers.length; i++) {
	let sum = 0;
	const dataType = dv.func.typeof(DQL.values[0][i])
	// check if we have a calculateable datatype - if not, skip the column
	if (!["number", "duration"].includes(dataType)) {
		sums.push("")
		continue;
	}
    // ... and for each row ...
	for (let k = 0; k < DQL.values.length; k++) {
		// get the current cell (row k and column i) and add it to the sum, if set
		let currentValue = DQL.values[k][i];
		if (currentValue) sum += currentValue 
	}
	if (!sum) sum = ""
	sums.push(dataType === "duration" ? luxon.Duration.fromMillis(sum) : sum);
}

// add a divider line for visual distinction between the query and the sums (thanks, Jillard!), add both to the table data
let hrArray = Array(DQL.headers.length).fill('<hr style="padding:0; margin:0 -10px;">');
DQL.values.push(hrArray)
DQL.values.push(sums)
//print the table
dv.table(DQL.headers, DQL.values)
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