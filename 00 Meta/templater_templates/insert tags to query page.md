<%*
const dvApi = app.plugins.plugins.dataview.api;
const dataviewRegex = /```(dataview(?:js)?)(.+?)```/gms;
const currFile = app.workspace.getActiveFile();
const content = await app.vault.cachedRead(currFile);

const datacommands = ["LIST", "TABLE", "TASK", "CALENDAR", "FROM", "WHERE", "FLATTEN", "SORT", "GROUP BY"];
const tags = [];
let tagprefix = "#dv/"

const queries = content.matchAll(dataviewRegex);
for (let query of queries) {
  const type = query[1];
  query = query[2];

  if (type === 'dataview') {
    datacommands.forEach(datacommand => {
      if (query.includes(datacommand)) {
        tags.push(`${tagprefix}${datacommand}`)
         // we only want to add this tag once, no need to check for the data command again here or in other queries
        datacommands.splice(datacommands.indexOf(datacommand), 1)
      }
    })
    const functions = query.matchAll(/([a-zA-Z]+)\(/g);
    addFunctionsTags(functions, tags)
  } else {
    tagprefix = "#dvjs/"
    const functions = query.matchAll(/dv\.([a-zA-Z]+)/g)
    addFunctionsTags(functions, tags)
  }
}
tR += tags.reduce((acc, curr) => `${acc} ${curr}`, "")

function addFunctionsTags(functions, tags) {
  for (let fn of functions) {
    const tag = `${tagprefix}${fn[1]}`
    if (!tags.contains(tag)) tags.push(tag)
  }
}
%>

