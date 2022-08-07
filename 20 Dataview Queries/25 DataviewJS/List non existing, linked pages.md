

---
description: shows all unresolved links (links to non existing pages), optionally with the files containing them
---
#dv/dataviewjs 


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


dv.table(["Unresolved Link", "Contained in"], Object.values(res).map(l => [l.link, l.usages]));
```

### List only unresolved link from a specific folder

> [!warning] Limitation when filtering unresolved links
> The second filter only works limited. When a file contains two unresolved links, i.e. "Fernando" and "Bob" and you're filtering after "Bob", you'll still end up with "Fernando" in the result, too - because they are both referenced from the same file and Bob's availability will keep the file and all its unresolved links in the filtered set.
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
	  return Object.keys(unresolvedLinks).filter(link => link.contains("na")).length
	})
  .forEach(([referingFile, unresolvedLink]) => process(referingFile, unresolvedLink));

dv.table(
  ["Non existing notes", "Linked from"],
  Object.entries(result).map(([unresolvedLink, referingFiles]) => [unresolvedLink, referingFiles.join(" • ")])
);
```