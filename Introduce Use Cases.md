# Introduce Use Cases

In order to make the vault better navigatable and give some more context to available queries as well as inspiration how these queries could be used, we want to introduce **Use Cases**. 

## What's a good topic for a Use Case?

Like the name says, a Use Case should be about some specific scenario you could achieve with dataview which requires (or can require) more than one dataview query. They should be **overviews for a topic**. Some examples:
- A Daily/Weekly/Quarterly Note (Template)
- A Music Album Overview page that provides information for songs, the album, the interpret, ...
- A persons page with informations about his birthday, the last contact with them, their interests, their relationships with other persons, ...
- Overview about a tv series, it's prequels and sequels, how many episodes you watched, when the new series comes out, participating actors, director, world, ... 

## Parts of a Use Case

A **Use Case** should consist of the following:

### A Use Case Page

The Use Case Page should explain what the Use Case is about, what its goal is, for what you could use it. It should collect all the queries via links that can be used for this Use Case, maybe with a little explanation why this query is useful.

### One or multiple example pages

To make it easier to understand the use case and to play around with it, a Use Case should provide at least one example page, where some of the collected queries are used. Feel free to generate test data for this like explained in [[Contribution#Add test data]].

## Structure of a Use Case

A Use Case should be created as a **folder** under **30 Dataview Resources/33 Use Cases**. For Example:

```
30 Dataview Resources/
  33 Use Cases/
    Basics of Dataview/ // <-- Use Case Folder
      Basics of Dataview.md // <-- Use Case Overview/Explanation Page
      Example1.md
      Example2.md
```

