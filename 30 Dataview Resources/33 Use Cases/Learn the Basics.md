
# Learn the Basics
This page shall guide you if you are a newcomer to the power of Dataview. **Before you start out**, make sure you made yourself familiar with the [official Documentation](https://blacksmithgu.github.io/obsidian-dataview/). While the documentation is not the most intuitive guide, it's important to get a grasp of the general idea and functionality to enable you writing your own queries. 

There is some [[Dataview Documentation and Resources|further reading]] you can dive into, but that's not necessary to get started. If you stumble across something, maybe the [[FAQ]] can help out.

## Understanding meta data on notes

Before you can start querying data from your vault, you need [**meta data**](https://blacksmithgu.github.io/obsidian-dataview/data-annotation/) to query. While there is already some information available on your [notes](https://blacksmithgu.github.io/obsidian-dataview/data-annotation/#implicit-fields) and [tasks](https://blacksmithgu.github.io/obsidian-dataview/data-annotation/#implicit-fields_1), to leverage the full power of dataview, you'll need to add your own meta data via the frontmatter or inline fields.

**Learn more about YAML Frontmatter** on the official documentation of Obsidian and take a look on our [[Frontmatter Overview]] and how [[Multivalue YAML Frontmatter Field]]s work.

**Learn more about Inline fields** in the [dataview documentation](https://blacksmithgu.github.io/obsidian-dataview/data-annotation/) .

## Basic Structure of Queries

A dataview query consists of following parts - in following order:

- exactly one **Query Type**
- depending on Query Type, zero, one or many **additional properties** for displaying
- zero or one **FROM** data command
- zero to many other **data commands**.

For more info about the general structure, refer to the [documentation](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#general-format).

### Understanding Query Types

The [**type of a query**](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#query-types) determines the format of your final output. We put together some basic examples you can play around with:

- [[Basic List Queries]]
- [[Basic Table Queries]]
- [[Basic Task Queries]]
- [[Basic Calendar Queries]]

### Understanding Data Commands

Beside the four **types** of a query, you can use [**data commands**](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#data-commands) to filter and enhance your query. There are some specialties to be aware of to successfully use them.

- [FROM](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#from) determines which notes to initially collect for your query depending on given [sources](https://blacksmithgu.github.io/obsidian-dataview/query/sources/)
- [WHERE](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#where) lets you filter notes based on information **inside** notes, i.e. meta data.
- [GROUP BY](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#group-by) lets you bundle up notes as one "result row" depending on a property (or calculation). See [[Example GROUP BY Queries]] for example usages.
- [FLATTEN](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#flatten) does the opposite of `GROUP BY` - instead of bundling up, it _splits_ notes depending on a property (or calculation). See [[Example FLATTEN Queries]] for example usages.
- [SORT](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#sort) sorts your result data depending on a property and a direction.
- [LIMIT](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#limit) lets you crop your result data to a desired (maximum) number. 

## Understanding Inline Queries

[**Inline Queries**](https://blacksmithgu.github.io/obsidian-dataview/data-queries/#inline-dql) are a special form of query. We'll showcase the basics in [[Basic Inline Queries]].

## Understanding JavaScript Queries

... would go way beyond the scope of this project 😉. [JavaScript Queries](https://blacksmithgu.github.io/obsidian-dataview/api/intro/) are an advanced technique, enabling you to create basically _anything_ if you have dataview, time and knowledge. JavaScript is a full-fledged programming language and learning it takes a huge commitment. 

**Don't fret, though!** The native dataview implementation is already immensely powerful and let you do a ton of complex querying right out of the box. You certainly do not need JavaScript to get started and you're probably fine for the rest of your journey without opening this pandora's box. 

If you *really* wish to get into **dataviewjs**, hop over to your favorite search engine, search for one of the various free basic courses in JavaScript, learn the basics, read the [dataviewjs documentation](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/) and get a glimpse of a world full of anarchy.