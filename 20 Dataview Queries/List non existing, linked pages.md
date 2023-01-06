---
description: shows all unresolved links (links to non existing pages), optionally with the files containing them
topics:
  - unresolved links
---
#dv/dataviewjs #dv/table #dv/from #dv/flatten #dv/where #dv/groupby #dvjs/flatMap #dvjs/sort #dvjs/list #dvjs/table


> [!hint] Basic query contributed [via Discord](https://discord.com/channels/686053708261228577/875721010144477204/1003441486492352572) [and Discord](https://discord.com/channels/686053708261228577/875721010144477204/1005583638177517628)

# List non existing links

## Basic 

As **DQL**:
```dataview
TABLE WITHOUT ID key AS "unresolved link", rows.file.link AS "referencing file"
FROM "10 Example Data"
FLATTEN file.outlinks as outlinks
WHERE !(outlinks.file) AND !(contains(meta(outlinks).path, "/"))
GROUP BY outlinks
```

As **dataviewjs:** (for a more similar result like the DQL solution, see variant "List the files the unresolved link is contained in")
```dataviewjs
const res = Object.values(app.metadataCache.unresolvedLinks)
.flatMap(unresolved => Object.keys(unresolved))
.sort(); 

const resSet = new Set(res).values();
dv.list(resSet);
```


## Variants

### List the files the unresolved link is contained in

> [!info] See Basic -> DQL for a pure DQL version of this result

```dataviewjs
const unresolvedLinksMap = app.metadataCache.unresolvedLinks

const res = {}
for (let page in unresolvedLinksMap) {
	const unresolved = Object.keys(unresolvedLinksMap[page]);
	if (unresolved.length === 0) continue;
	for (let link of unresolved) {
		if (!res[link]) res[link] = {link, usages: []}
		res[link].usages.push(dv.fileLink(page))
	}
}


dv.table(["Unresolved Link", "Contained in"], Object.values(res).map(l => [dv.fileLink(l.link), l.usages]));
```

#### Sort the results by count of references
This version sorts the unresolved links by the count on how much they appear in other files. It also shows a direct file link to create the file and condenses the references for easier viewing.

```dataviewjs
const unresolvedLinksMap = app.metadataCache.unresolvedLinks

const res = {}

for (let page in unresolvedLinksMap) {
	const unresolved = Object.keys(unresolvedLinksMap[page]);
	
	if (unresolved.length === 0) {
    	continue;
    }
    	
	for (let link of unresolved) {
		if (!res[link]) {
    		res[link] = {link, usages: []}
    	}
    	
		res[link].usages.push(dv.fileLink(page))
	}
}

const rows = Object.values(res)
    .map(l => [dv.fileLink(l.link), l.usages.join(' · '), l.usages.length])
    .sort((a, b) => a[2] > b[2] ? -1 : 1)

dv.table(
    ["Unresolved Link", "Contained in", "Count"], 
    rows
);
```

### List only unresolved links from a specific folder meeting specific criteria

#### As DQL
```dataview
TABLE WITHOUT ID key AS "unresolved link", rows.file.link AS "referencing file"
FROM "10 Example Data"
FLATTEN file.outlinks as outlinks
WHERE startswith(meta(outlinks).path, "B") AND length(meta(outlinks).path) > 3
WHERE !(outlinks.file) AND !(contains(meta(outlinks).path, "/"))
GROUP BY outlinks
```


#### As DataviewJS
> [!warning] Limitation when filtering unresolved links in DataviewJS
> The second filter only works limited. When a file contains two unresolved links, i.e. "Fernando" and "Bob" and you're filtering after "Bob", you'll still end up with "Fernando" in the result, too - because they are both referenced from the same file and Bob's availability will keep the file and **all** its unresolved links in the filtered set.
> In order to fix that, it'd be necessary to filter out the unresolvedLinks array and map it back to the object that'll be processed.

```dataviewjs
let result = {};

function process(referingFile, unresolvedLinks) {
  Object.keys(unresolvedLinks).forEach(function (link) {
    link = dv.fileLink(link);
    if (!result[link]) result[link] = [];
    
    result[link].push(dv.fileLink(referingFile));
  });
}

Object.entries(dv.app.metadataCache.unresolvedLinks)
  .filter(([referingFile]) => {
    return referingFile.startsWith("10 Example Data/dailys")
  })
  .filter(([_, unresolvedLinks]) => {
	  return Object.keys(unresolvedLinks)
	  .filter(link => link.startsWith("B") && link.length > 3)
	  .length
	})
  .forEach(([referingFile, unresolvedLink]) => process(referingFile, unresolvedLink));

dv.table(
  ["Non existing notes", "Linked from"],
  Object.entries(result).map(([unresolvedLink, referingFiles]) => [unresolvedLink, referingFiles.join(" • ")])
);
```

### List unresolved links, sorted by name, excluding certain folders and notes

#### As DataviewJS
```dataviewjs
let result = {};

function process(referingFile, unresolvedLinks) {
  Object.keys(unresolvedLinks).forEach(function (link) {
    link = dv.fileLink(link);
    if (!result[link]) result[link] = [];

    result[link].push(dv.fileLink(referingFile));
  });
}

Object.entries(dv.app.metadataCache.unresolvedLinks)
  .filter(([referingFile]) => {
    return !referingFile.startsWith("00 Meta") && !referingFile.startsWith("30 Dataview Resources/31 Query Overviews/Use Case Overview")
  })
  .forEach(([referingFile, unresolvedLink]) => process(referingFile, unresolvedLink));


const rows = Object.entries(result)
    .map(([unresolvedLink, referingFiles]) => [unresolvedLink, referingFiles])
    .sort((a, b) => a[0] > b[0] ? 1 : -1)

dv.table(
    ["Unresolved Link", "Contained in"],
	rows
);
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
