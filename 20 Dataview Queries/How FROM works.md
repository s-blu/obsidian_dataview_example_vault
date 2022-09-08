`FROM` is a special **data command**. It is special because unlike the other data commands, you can use `FROM` only once.

> [!info] A query has **zero or one** `FROM` statements.

## Purpose

`FROM` lets you query for specific pages you want to include in your query. You can use **Folders** and **Tags** or any combination with `AND` and `OR` of these to determine which pages should be taken into account for your query.

## Usage

You declare `FROM` right after your Query Type (and possible additional properties), i.e.

```
LIST
FROM ...
WHERE/FLATTEN/GROUP BY/SORT/LIMIT
```

It is **not allowed** to place `FROM` **after** any other data command - it needs to be the first one!

Valid arguments for a `FROM` are **tags, folders, files and links**. See the [documentation](https://blacksmithgu.github.io/obsidian-dataview/query/queries/#from) for more infos on that.

> [!done] Valid Usages
> `FROM "Folder Name 1"`
> `FROM #tag1`
> `FROM [[Learn the Basics]]`
> `FROM outgoing([[Learn the Basics]]`
> `FROM "path/to/specific/file"`
> `FROM [[]]`
> `FROM outgoing([[]])`
> 
> `FROM "Folder Name 1" OR "Folder Name 2"`
> `FROM "Folder Name 1" AND "Folder Name 2"`
> `FROM "Folder Name 1" OR #tag1`
> `FROM "Folder Name 1" AND #tag1`
> `FROM ("Folder Name 1" OR #tag1) AND ((#tag2 OR #tag3 OR #tag4) OR "Folder Name 2)"`
> `FROM #tag1 AND -"path/to/file" AND -"Folder Name 1"`

> [!error]  `this` is not available inside `FROM`
> `FROM this.file.name` won't work.
>

> [!error] Meta data is not available in `FROM`
> goodDay:: yes
> 
> `FROM goodDay` won't work.

## Good to know

- Can be used only once (but can also be omitted)
- Needs to be on a specific place in the query
- Is the fastest way (performant wise) to filter for pages