# Queries by DQL function

```dataviewjs
const tagsToDisplay = ["object","list","date","dur","number","string","link","embed","elink","typeof","round","contains","extract","sort","reverse","length","sum","all","any","none","join","filter","map","regexmatch","regexreplace","replace","lower","upper","split","startswith","endswith","padleft","padright","substring","truncate","default","choice","striptime","localtime","meta"]

for (let tag of tagsToDisplay) {
	dv.header(2, tag)
	dv.table(["File", "Description"], dv.pages('"20 Dataview Queries" AND #dv/' + tag).map(p => [p.file.link, p.description]))
}
```
