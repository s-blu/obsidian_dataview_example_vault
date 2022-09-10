---
description: Search for a word or combination of words in your notes complete content, not only meta data!
topics:
  - analyzing file content
---
 #dv/dataviewjs #dvjs/pages #dvjs/io #dvjs/table 

> [!hint] Contributed by erazlogo and mnvwvnm

# Search for words in your files content across your vault

## Basic 

> [!attention] Crawling file content of all queried files
> This query goes beyond the regular boundaries of dataview by crawling the raw file content. That means you can search for words independent of their usage in tags or meta data. **Crawling the page content can be a memory intense operation**, so it's important to use a path or tag in `dv.pages()` to avoid iterating over the whole vault. Except your computer can stand that, of course. 😉

```dataviewjs
const word = "Queries" // <-- Type your search between the ""

// We need to double-escape \b here so it's correctly fed into RegExp after the concationation (as "\b" and not as "b").
const regex = new RegExp("\\b" + word + "\\b", "gi")
// Query pages and crawl their raw data content 
const pages = await Promise.all(
    dv.pages('"30 Dataview Resources"')
    .map(async (page) => {
        const content = await dv.io.load(page.file.path);
        // Map pages to a custom object - if you want to have more infos in the
        // table below, you need to add them here!
        return {
            link: page.file.link,
            count: ( content.match(regex) || []).length
        };
    })
)
// Render the result table 
dv.table(
        ["Note", `Matches for "${word}"`],
            pages
            .filter(p => p.count)
            .sort((a, b) => b.count - a.count)
            .map(p => [p.link, p.count])  
    );
```

## Variants

### Display matching lines and surrounding words for context

> [!info] Increasing number of surrounding words
> To see more surrounding words, increase the second number in the regular expression in the curly brackets. You can set it i.e. to `{0,5}` to see up to five surrounding words.

```dataviewjs
const word = "but"

const regex = new RegExp("(\\S+\\s?){0,2}(\\b"+word+"\\b)(\\s\\S+){0,2}", "gi")
const pages = await Promise.all(
    dv.pages('"30 Dataview Resources"')
    .map(async (page) => {
        const content = await dv.io.load(page.file.path);
        const matches = content.match(regex);
        return {
            link: page.file.link,
            count: ( matches || []).length,
            matches
        };
    })
)

dv.table(
        ["Note", "Count", `Matches for "${word}"`],
            pages
            .filter(p => p.count)
            .sort((a, b) => b.count - a.count)
            .map(p => [p.link, p.count, p.matches])  
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
