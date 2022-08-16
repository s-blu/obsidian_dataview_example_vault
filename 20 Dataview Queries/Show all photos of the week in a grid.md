---
description: Show all images you have in your daily notes for this week in an image grid 
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
const pages = dv.pages('"10 Example Data/dailys"').where(p => p.day && p.day.year == yearAndWeek[0] && p.day.weekNumber == yearAndWeek[1])
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

> [!info] Sources of this query
> You'll find the sources of this dv.view snippet under `00 Meta/dataview_views/imagegrid`. dv.views are a possibility to reuse complex javascript queries and to add css styling to them. Read more [here](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/#dvviewpath-input)

```dataviewjs
await dv.view('00 Meta/dataview_views/imagegrid')
```