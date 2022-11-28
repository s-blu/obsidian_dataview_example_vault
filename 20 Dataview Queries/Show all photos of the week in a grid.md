---
description: Show all images you have in your daily notes for this week in an image grid 
topics:
  - images
  - grid view
  - weekly aggregation
---
#dv/dataviewjs #dvjs/pages #dvjs/where #dvjs/container #dvjs/list #dvjs/view


# Show all photos of the week in a grid

## Basic 

> [!attention] Additional CSS Snippet required
> A CSS Snippet is in place to style this query. You'll find it under `.obsidian\snippets\show-photos-of-the-week-as-grid.css`  as well as below. [Read more about how to use CSS Snippets](https://help.obsidian.md/How+to/Add+custom+styles#Use+Themes+and+or+CSS+snippets)

> [!info] Usage in a weekly note
> When you want to use this query in a weekly note and your weekly note is named like "2022W2", use this as the first line: 
> `const yearAndWeek = dv.current().file.name.split('-W')`
>  This will retrieve the year and weeknumber information from your file name and you do not need to adjust this manually.

```dataviewjs
const yearAndWeek = ["2022", "02"]
const pages = dv.pages('"10 Example Data/dailys"').where(p => p.file.day && p.file.day.year == yearAndWeek[0] && p.file.day.weekNumber == yearAndWeek[1])
dv.container.className += ' imagegrid'
dv.list(pages.picoftheday)
```

### Used CSS Snippet

```css
.imagegrid ul {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}

.imagegrid ul li {
  display: flex;
  flex-direction: column;
}

.imagegrid ul li::marker {
  content: "";
}

/* I wanted to ignore the width on the images and set a fixed one for them.
Remove if you want to preserve the width configured on the image link itself. */
.imagegrid ul li img,
.markdown-rendered img:not([width]) {
  max-width: 200px;
}
```

## Variants

### Use as view snippet with a library for a nice layout

![[What is#^dv-view]]

> [!warning] Adjustment of script necessary
> For demonstration purposes, the variable "yearAndWeek" is hardcoded to ["2022", "2"]. In order to use the script inside your vault, you need to adjust this line as explained inside the script.
```dataviewjs

await dv.view('00 Meta/dataview_views/imagegrid', { current: dv.current(), dailyNotesSearchQuery: '"10 Example Data/dailys"', metadatafield: 'picoftheday'})
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