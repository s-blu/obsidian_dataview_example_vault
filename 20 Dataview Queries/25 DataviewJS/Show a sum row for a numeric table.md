---
description: Show a seperate sum row for numeric tables
---
#dv/dataviewjs 

# Show a sum row for a numeric table

## Basic 

> [!attention]
> This only renders a sum row, not the values beforehand. You need a separate table query for this - please see "Example"

```dataviewjs
const nameOfRow = "Sums";
const fieldsToSumUp = ["valA", "valB", "something"] // <- put the fields  of your table here
const pages = dv.pages('"10 Example Data"').where(p => p.valA) // <- replicate the "FROM" and "WHERE" of your previous table to get the same result set

// you don't need to touch this, normally.
const sums = [nameOfRow];
for (let field of fieldsToSumUp) {
	let sum = pages.array().map(p => p[field]).reduce((curr, acc) => acc + curr, 0);
	if (!sum) sum = ""
	sums.push(sum);
}
dv.container.className += ' sum-only-table'
dv.table(["", ...fieldsToSumUp], [sums])
```

## Example

> [!info] 
> To align the total column and the columns of the query before, change the text or length of the "Sums" placeholder

```dataview
TABLE situps, steps
FROM "10 Example Data/dailys"
WHERE file.day.month = 2
```

```dataviewjs
const nameOfRow = "Sums";
const fieldsToSumUp = ["situps", "steps"] 
const pages = dv.pages('"10 Example Data/dailys"').where(p => p.file.day.month === 2)

// you don't need to touch this, normally.
const sums = [nameOfRow];
for (let field of fieldsToSumUp) {
	let sum = pages.array().map(p => p[field]).reduce((curr, acc) => acc + curr, 0);
	if (!sum) sum = ""
	sums.push(sum);
}
dv.container.className += ' sum-only-table'
dv.table(["", ...fieldsToSumUp], [sums])
```

### CSS

You can add some CSS to highlight the total row and make it a bit less space intensive


```css
.sum-only-table .table-view-table > thead > tr > th {
  visibility: hidden;
}

.sum-only-table .table-view-table > tbody > tr > td {
  font-weight: bold;
  text-transform: uppercase;
  color: var(--text-accent);
}
```