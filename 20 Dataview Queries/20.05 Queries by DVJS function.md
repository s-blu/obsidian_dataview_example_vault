# Queries by DVJS function

```dataviewjs
const tagsToDisplay = ["current", "pages", "pagePaths", "page", "el", "header", "paragraph", "span", "execute", "executeJs", "view", "list", "taskList", "table", "markdownTable", "markdownList", "markdownTaskList", "isArray", "fileLink", "sectionLink", "blockLink", "date", "duration", "compare", "equal", "clone", "parse", "csv", "load", "normalize", "query", "tryQuery", "queryMarkdown", "tryQueryMarkdown", "tryEvaluate", "evaluate","length", "where", "filter", "map", "flatMap", "mutate", "limit", "slice", "concat", "indexOf", "find", "findIndex", "includes", "join", "sort", "groupBy", "distinct", "every", "some", "none", "first", "last", "to", "expand", "forEach", "array"]

tagsToDisplay.sort()

for (let tag of tagsToDisplay) {
	dv.header(2, tag)
	dv.table(["File", "Description"], dv.pages('"20 Dataview Queries" AND #dvjs/' + tag).map(p => [p.file.link, p.description]))
}
```