# Use Cases

In order to make the vault better navigable and give some more context to available queries as well as inspiration how these queries could be used, we want to introduce **Use Cases**. 

## What's a good topic for a Use Case?

Like the name says, a Use Case should be about some specific scenario you could achieve with dataview, which requires (or can require) more than one dataview query. They should be **overviews for a topic**. Some examples:
- A Daily/Weekly/Quarterly Note (Template)
- A Music Album Overview page that provides information for songs, the album, the artist, ...
- A persons page with information about his birthday, the last contact with them, their interests, their relationships with other people, ...
- Overview about a TV series, it's prequels and sequels, how many episodes you watched, when the new series comes out, participating actors, director, world, ... 

### Difference between a query page and a use case

If you have trouble deciding if your contribution should be a query page under `20 Dataview Queries` or rather a Use Case, try the following:  Start with a Query Page like described [[Contribution#Add a query|here]]. Write your query name and description. Can you narrow down your contribution to one specific sentence? Then you should use a query page. Do you end up with a sentence like "Should do this or that or this other thing _and_ something else, but also different fancy things", you probably about to describe a use case consisting of **multiple, different query pages**. 

As a rule of thumb: A **use case** describes a scenario, a **broader field**, probably is a complete note in a real vault. A **query** (page) has a very specific goal and **achieves one specific thing** that'll probably end up as a **part** of a page.  

## Parts of a Use Case

A **Use Case** should consist of a **Use Case Page** and one or more **Example pages** that show the use case "in action".

### A Use Case Page

The Use Case Page should explain what the Use Case is about, what its goal is, for what you could use it. It should collect all the queries via links that can be used for this Use Case, maybe with a little explanation why this query is useful.

### One or multiple example pages

To make it easier to understand the use case and to play around with it, a use case should provide at least one example page, where some of the collected queries are used. Feel free to generate test data for this like explained in [[Contribution#Add test data]].

## Structure of a Use Case

A Use Case should be created as a **folder** under **30 Dataview Resources/33 Use Cases**. For Example:

```
30 Dataview Resources/
  33 Use Cases/
    Enhance your daily note/ // <-- Use Case Folder
      Enhance your daily note.md // <-- Use Case Overview/Explanation Page
      Example1.md
      Example2.md
```

If a Use Case, for whatever (good) reason does **not** have and will not have examples, skip the folder and place the Use Case Overview directly under **30 Dataview Resources/33 Use Cases**:

```
30 Dataview Resources/
  33 Use Cases/
    Basics of Dataview.md // <-- Use Case Overview/Explanation Page
```