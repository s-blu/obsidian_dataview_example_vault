

---
description: shows all unresolved links (links to non existing pages), optionally with the files containing them
---
#dv/dataviewjs 


> [!hint] Basic query contributed [via Discord](https://discord.com/channels/686053708261228577/875721010144477204/1003441486492352572) 

# List non existing links

## Basic 
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