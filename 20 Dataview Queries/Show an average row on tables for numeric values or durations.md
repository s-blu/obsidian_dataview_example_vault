---
description: Show a average row for numeric values and durations
topics:
  - summary row
---
 #dv/dataviewjs #dvjs/tryQuery #dvjs/func #dvjs/table

# Show an average row on tables for numeric values or durations

## Basic 

```dataviewjs
// Paste your DQL for the table here:
const query = `TABLE praying, training, situps, steps
FROM "10 Example Data/dailys"
WHERE file.day.month = 2`
// change the name of the total row, if you like:
const nameOfTotalRow = "Avg";
// change how many digits you want to see after comma
const digitAfterComma = 1;

// you don't need to touch this, normally.
// get the data from the query above
let DQL = await dv.tryQuery(query);
const sums = [nameOfTotalRow];
// for each header (except the first one, which is "File")...
for (let i = 1; i < DQL.headers.length; i++) {
	let sum = 0;
	let count = 0;
	const dataType = getDatatypeOfColumn(i, DQL.values)
	// check if we have a calculateable datatype - if not, skip the column
	if (!["number", "duration"].includes(dataType)) {
		sums.push("")
		continue;
	}
    // ... and for each row ...
	for (let k = 0; k < DQL.values.length; k++) {
		// get the current cell (row k and column i) and add it to the sum, if set
		let currentValue = DQL.values[k][i];
		if (currentValue) {
		  sum += currentValue;
		  count++;
	    }
	}
	let avg = sum ? (sum / count).toFixed(digitAfterComma) : "";
	sums.push(dataType === "duration" ? luxon.Duration.fromMillis(avg) : avg);
}

function getDatatypeOfColumn(columnNo, values) {
	let i = 0;
	let datatype;
	while (i < DQL.values[0].length && (!datatype || datatype === "null")) {
		datatype = dv.func.typeof(DQL.values[i][columnNo])
		i++;
	}
	return datatype;
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
