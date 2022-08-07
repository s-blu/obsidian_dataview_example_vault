---
description: Calculate the sum of multiple times (hh:mm), i.e. the sum of hours one has spent on a project 
---
#dv/dataviewjs 

# Calculate Sum of working hours for a project

## Basic 

```dataviewjs
const projects = dv.pages('"10 Example Data/projects"')
	.mutate(p => p.workHourSum = sumUpWorkHours(p["working hours"]))


dv.table(["Project", "Working Hours", "Sum Working Hours"], 
		 projects.map(p => [p.file.link, p["working hours"], p.workHourSum]))

function sumUpWorkHours(workingHours) {
	const durations = workingHours
		.split(",")
		.map(h => dv.luxon.Duration.fromISOTime(h.trim()));
	
	const sum = durations.reduce((acc, curr) => acc + curr, 0)
	return dv.luxon.Duration.fromMillis(sum) 
}
```