<%*
const dvApi = app.plugins.plugins.dataview.api;
const dataviewRegex = /```(dataview(?:js)?)(.+?)```/gms;
const currFile = app.workspace.getActiveFile();
const content = (await app.vault.cachedRead(currFile)).split("%% === end of query page === %%")[0];

const datacommands = ["LIST", "TABLE", "TASK", "CALENDAR", "FROM", "WHERE", "FLATTEN", "SORT", "GROUP BY"];
const tags = [];
let tagprefix = "#dv/"

if (content.match(/`\$= [^`]+`/)) {
  tags.push(tagprefix + 'inlinejs')
}
if (content.match(/`\= [^`]+`/)) {
  tags.push(tagprefix + 'inline')
}

const queries = content.matchAll(dataviewRegex);
for (let query of queries) {
  const type = query[1];
  query = query[2];

  if (type === 'dataview') {
    datacommands.forEach(datacommand => {
      if (query.includes(datacommand)) {
        tags.push(`${tagprefix}${datacommand.replace(/\s/, '')}`)
         // we only want to add this tag once, no need to check for the data command again here or in other queries
        datacommands.splice(datacommands.indexOf(datacommand), 1)
      }
    })
    const functions = query.matchAll(/([a-zA-Z]+)\(/g);
    addFunctionsTags(functions, tags)
  } else {
	addTag('dataviewjs')
    tagprefix = "#dvjs/"
   
    const functions = query.matchAll(/dv\.([a-zA-Z]+)/g)
    addFunctionsTags(functions, tags)
  }
}
tR += tags.reduce((acc, curr) => `${acc} ${curr}`, "")

function addFunctionsTags(functions) {
  for (let fn of functions) {
    addTag(fn[1])
  }
}

function addTag(subtag) {
	const tag = `${tagprefix}${subtag}`
    if (!tags.contains(tag)) tags.push(tag)
}
%>