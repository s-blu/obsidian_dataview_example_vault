---
description: This page is a fancy setup for notes you want to make on music videos. It renders song information and embeds a youtube video.
topics:
  - embed
  - video
---
#dv/dataviewjs #dvjs/current #dvjs/span 


> [!hint] Contributed by Daniel.
> Discord: `dbarenholz#2331`
> Find me [here](https://www.dbarenholz.com).

# `$=dv.span(dv.current().artist)` - `$=dv.span(dv.current().title)`

>[!info]- Song Information
> title:: Never Gonna Give You Up
> artist:: Rick Astley
> vocalist:: Rick Astley
> album:: Whenever You Need Somebody
> number:: 1
> yt:: https://www.youtube.com/embed/watch?v=dQw4w9WgXcQ


## Basic 

```dataviewjs
const me = dv.current()
dv.span(`The song *${me.title}*, composed by *${me.artist}* and sung by *${me.vocalist}* is number *${me.number}* of the album *${me.album}*. A video is shown below.`)
dv.span(`<iframe width="560" height="315" src="${me.yt}?modestbranding=1&hl=en&persist" title="${me.artist} - ${me.title}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`)
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
const inlinksFromUseCases = dv.current().file.inlinks.filter(link => link.path.contains("33 Use Cases"));

const header = `> [!info] Part of Use Cases`;

if (inlinksFromUseCases.length > 1) {
	const list = inlinksFromUseCases.array().reduce((acc, curr) => `${acc}</br> - ${curr}`,"")

	dv.span(`${header}
    > This query is part of following use cases:
    > ${list}
    > 
	`)
} else if (inlinksFromUseCases.length === 1) {
	dv.span(`${header}
    > This query is part of use case ${inlinksFromUseCases[0]}.
	`)
}
```