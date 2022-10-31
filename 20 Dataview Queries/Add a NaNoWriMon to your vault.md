---
description: A progress bar that grows with your progress to track of your writing projects
topics:
  - custom output
  - progress bar
---
#dv/dataviewjs #dvjs/page #dvjs/el #dvjs/current

# Add a NaNoWriMon to your vault

> [!info] About NaNoWriMons
> NaNoWriMons are a inofficial, motivational help for participants of NaNoWriMo. Beside tracking your progress it adds a pokémon of your choice that grows with your progress. You'll find the original [here](https://thousandroads.net/fanfic/nanowrimon/)

## Basic 

> [!info] Local image files
> To save us from fetching the image pictures from the web all the time, this query assumes that you have them local and inside your configured attachment folder. This has the advantage that your mascot do not need to be a Pokémon but can be whatever you choose!

wordcount:: 3500
targetcount:: 15000

```dataviewjs
const pagePath = "Add a NaNoWriMon to your vault" // the page path from vault root
const inlineWordcount = "wordcount"; // the field your wordcount is saved in
const inlineTargetCount = "targetcount" // the field your target count is saved in
const name = "Bulba"; // The name of your mon
const images = ["Pokémon-Icon_001.png", "Pokémon-Icon_002.png", "Pokémon-Icon_003.png"] // Image file names to use for your mon. needs to be three and they need to be saved in your attachments folder


// rendering, doesn't need to be adjusted 
const page = dv.page(pagePath);
let image = images[0];
const percentage = Math.round(page[inlineWordcount] / page[inlineTargetCount] * 100);
if (percentage > 33 && percentage < 66) {
	image = images[1]
} else if (percentage > 66) {
	image = images[2]
}

const attachments = this.app.vault.getConfig("attachmentFolderPath");
const basePath = this.app.vault.adapter.basePath

const html = `<div class="monwrapper" style="display:flex;align-items:center;">
<img src="${basePath}/${attachments}/${image}" class="mon" style="margin-right:10px;"></img>
<div>
<div class="monname">${name}</div>
<div class="progressbar"><progress max="100" value="${percentage}"></progress> Lv. ${percentage}</div></div>
</div>`;
dv.el("div", html)
```

## Variants

### Use any amount of images

The Basic Variant is set to use three images. With this variant the breakpoints on which percentage the next image will be shown gets calculated automatically depending on the amount of images specified and thus support i.e. Pokémon with two evolutions or image series of any number.

```dataviewjs
const pagePath = "Add a NaNoWriMon to your vault" // the page path from vault root
const inlineWordcount = "wordcount"; // the field your wordcount is saved in
const inlineTargetCount = "targetcount" // the field your target count is saved in
const name = "Story Progress"; // The name of your mon
const images = ["flower_growth/flowergrowth1.png", "flower_growth/flowergrowth2.png","flower_growth/flowergrowth3.png","flower_growth/flowergrowth4.png","flower_growth/flowergrowth5.png","flower_growth/flowergrowth6.png"] // Image file names to use for your mon. 


// rendering, doesn't need to be adjusted 
const page = dv.page(pagePath);
let image = images[0];
const percentage = Math.round(page[inlineWordcount] / page[inlineTargetCount] * 100);
if (images.length > 1) {
	const breakpoint = 100 / images.length;
	let i = 0;
	let currentBreakpoint = (i + 1) * breakpoint;
	while (percentage > currentBreakpoint && currentBreakpoint <= 100) {
		i++;
		currentBreakpoint = (i + 1) * breakpoint;
	}
	image = images[i]
} 

const attachments = this.app.vault.getConfig("attachmentFolderPath");
const basePath = this.app.vault.adapter.basePath

const html = `<div class="monwrapper" style="display:flex;align-items:center;">
<img src="${basePath}/${attachments}/${image}" class="mon" style="margin-right:10px;"></img>
<div>
<div class="monname">${name}</div>
<div class="progressbar"><progress max="100" value="${percentage}"></progress> Lv. ${percentage}</div></div>
</div>`;
dv.el("div", html)
```

### Use the current page as source

```dataviewjs
const inlineWordcount = "wordcount"; // the field your wordcount is saved in
const inlineTargetCount = "targetcount" // the field your target count is saved in
const name = "Bulba"; // The name of your mon
const images = ["Pokémon-Icon_001.png", "Pokémon-Icon_002.png", "Pokémon-Icon_003.png"] // Image file names to use for your mon. needs to be three and they need to be saved in your attachments folder


// rendering, doesn't need to be adjusted 
const page = dv.current();
let image = images[0];
const percentage = Math.round(page[inlineWordcount] / page[inlineTargetCount] * 100);
if (percentage > 33 && percentage < 66) {
	image = images[1]
} else if (percentage > 66) {
	image = images[2]
}

const attachments = this.app.vault.getConfig("attachmentFolderPath");
const basePath = this.app.vault.adapter.basePath

const html = `<div class="monwrapper" style="display:flex;align-items:center;">
<img src="${basePath}/${attachments}/${image}" class="mon" style="margin-right:10px;"></img>
<div>
<div class="monname">${name}</div>
<div class="progressbar"><progress max="100" value="${percentage}"></progress> Lv. ${percentage}</div></div>
</div>`;
dv.el("div", html)
```

### Use the size of the current page as character count

> [!attention] Character count instead of word count
> This variant is based on a character count instead of a word count. We do not have any information about the word count available automatically.

> [!attention] Usage of file.size
> We use file.size here to automatically read the character count of the current page. Please mind that the file.size property is _not_ equals the character count you see in the status bar, but only near it. If you want to have exact numbers, you need to track your progress manually with the Variant above. If you're fine with an estimate, this variant saves you the trouble of updating your current character count.

```dataviewjs
const inlineTargetCount = "targetcount" // the field your target count is saved in
const name = "Belli"; // The name of your mon
const images = ["Pokémon-Icon_069.png", "Pokémon-Icon_070.png", "Pokémon-Icon_071.png"] // Image file names to use for your mon. needs to be three and they need to be saved in your attachments folder


// rendering, doesn't need to be adjusted 
const page = dv.current();
let image = images[0];
const percentage = Math.round(page.file.size / page[inlineTargetCount] * 100);
if (percentage > 33 && percentage < 66) {
	image = images[1]
} else if (percentage > 66) {
	image = images[2]
}

const attachments = this.app.vault.getConfig("attachmentFolderPath");
const basePath = this.app.vault.adapter.basePath
const html = `<div class="monwrapper" style="display:flex;align-items:center;">
<img src="${basePath}/${attachments}/${image}" class="mon" style="margin-right:10px;"></img>
<div>
<div class="monname">${name}</div>
<div class="progressbar"><progress max="100" value="${percentage}"></progress> Lv. ${percentage}</div></div>
</div>`;
dv.el("div", html)
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
