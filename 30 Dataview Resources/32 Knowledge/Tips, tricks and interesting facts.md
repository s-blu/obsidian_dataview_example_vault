# Tips, tricks and interesting facts

## Metadata and Case Sensitivity
> [!hint] Metadata fields with capital letters  are available in their original and a lowercase form
> For example, if you add `wentToSleep:: 22:30`, you can access this field in your query via `wentToSleep` or `wenttosleep` - but not as `wenttoSleep` etc!

```dataview
TABLE wentToSleep, wenttosleep, wentTosleep, wenttoSleep, WentToSleep, went-to-sleep
WHERE file.name = "2022-01-05"
```
```dataview
TABLE capitalized, Capitalized, CapitalizedMetadata, capitalizedMetadata, capitalizedmetadata
FROM "10 Example Data/dailys"
WHERE file.name = "2022-01-20"
```

## Inspecting available fields
> [!hint] Inspect available fields of your current (or any) file
> You can do this either with `dv.span(dv.current())` for the current file or `dv.span(dv.page('nameOfPage')` for any other file. For better readability, you can also use the developer console for printing it: use `console.log("Current Page:", dv.current())` and open the console via SHIFT CTRL I. 
> Please mind: This only works as a dataviewjs block - or a javascript inline field! 

**As js inline query to the console (hit SHIFT + CTRL + I)**
`$= console.log("Current Page:", dv.current())`

**As span inside the document** (add `dataviewjs` to the block to see a result - the output is lengthy!)
```
dv.span(dv.page("2022-01-05"))
```

## The difference between \`=[[]]\` and \`=this\`

In DQL inline code, \`=[[]]\` doesn't output anything, but \`=[[]].file\` or \`=[[]].something\` does. It is because \`=[[]]\` is showing an empty link. If you index it (by using ".something") you get the current file, probably because the author just makes it refer to the current page like "this" instead of throwing an error. While \`=this\` is referring to the current page metadata like what \`\$= dv.current()\` does. The reason why \`=[[]].something\` works is that you can do stuff like \`=[[Peter]].lastname\` inside another note (comparable with \`$=dv.page("Peter").lastname\`).