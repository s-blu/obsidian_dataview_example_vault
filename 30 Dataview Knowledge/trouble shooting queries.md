# trouble shooting queries

Your query is not behaving like it should be? We have some tips on how to find out what's going wrong.

## Query returns 0 results, but the data is there.

There needs to be something in your query that filters out or hides your data.

### 1. Try to remove the FROM clause.
First, remove your `FROM` statement altogether. Does the result you expect show up now (probably among others, not wanted)? Add every `FROM` expression back one by one.

For example, you have `FROM #dv AND "20 Dataview Queries"`, first add only `FROM #dv`. Your result is still there? Try `FROM #dv AND "20 Dataview Queries"` - do your expected pages vanish? Then the FROM clause - maybe in **combination** with the `WHERE` clause - is causing trouble. So next...

### 2. Try to remove the WHERE clause.
Secondly, remove your `WHERE` clause but keep your `FROM` statement. Are the results still gone? Then your `FROM` statement is erroneous. Try to find the erroneous part and have a look at your data why they might get filtered out by it.

Your data is there, if you keep the `FROM`, but delete the `WHERE`? Then your `WHERE` statement is acting up. Add every `WHERE` expression back one by one.

For example you have `WHERE file.name != this.file.name AND #tag1 AND someMetadata`, then add first `WHERE file.name != this.file.name`. The data you're expecting still there? Try `WHERE file.name != this.file.name AND #tag1`. Still there? No? The last added part of the `WHERE` clause (`AND #tag1`) causes some trouble.


### 3. Print out the metadata of your page. 

You found the error, but don't understand why it causes problems? It might help if you print out your current page like dataview sees it, to understand the structure of available metadata. You can do that in different approaches:

If you're writing a table-query, **add the metadata you're using in your `WHERE` as a table column** and see if the values match your expectation.

To **see the whole current page with all its properties and metadata**, add 

```dataview
LIST this
WHERE file.name = this.file.name
```

or, when using dataviewJS queries, try

`$= console.log("Current file:", dv.current())`

and open the developer console with `CTRL SHIFT I`.


## Query shows some kind of error

> [!hint] Open up read and edit mode side by side
> These examples are observed best when you switch to "[Edit Mode](https://help.obsidian.md/How+to/Read+and+edit+modes)" and open up a second pane in read mode - otherwise you'll only see the error or the dataview query :) 


Read the error description carefully. There is a little arrow pointing at the erroneous place. For example:

```dataview
TABLE
WHERE #dv/list
```

The little arrow is pointing at the # - because WHERE cannot work with a plain tag. You need to tell WHERE what to do with this tag.

```dataview
TABLE
WHERE contains(file.tags, "#dv/list"
```

Here, we do not have a little arrow, but only a error message: `Got the end of the input`. This normally means that an input ended (because the query is over) without dataview expecting it. On the last line you'll find what the plugin would've expected instead of the end of the query. We are missing the closing `)`

```dataview
TABLE
WHERE contains(file.tags, "#dv/calendar")
```

Solved! 🎉

**Another example**:

```dataview
LIST sum
FROM "10 Example Data/dailys"
WHERE paid
FLATTEN sum() as sum
```

It tells us that our `WHERE` clause failed and shows us the **first three errors** why. Here, it's the same one three times. 

Let's read this message: `No implementation of 'sum' found for arguments:`
It's rather technical. What it tries to tell you: "I don't know what to do with these arguments: (none)" - because you did not give any arguments inside the round brackets.

Lets try this: 

```dataview
LIST sum
FROM "10 Example Data/dailys"
WHERE paid
FLATTEN sum(paid, paid) as sum
```

Now our error message is a bit different and the first three aren't completely equal anymore. It now says "I don't know what to do with two things that are null and null - or array and array - or string and string"

So the `sum` function doesn't know how to handle our input. How to solve this?
First, head over to the [official dataview documentation and read up how sum works](https://blacksmithgu.github.io/obsidian-dataview/query/functions/#sumarray):

> [!cite]
> ### `sum(array)`
> Sums all numeric values in the array
> ```
> sum(list(1, 2, 3)) = 6
> ```

We've learned two important things here: First, **sum expects exactly one argument**. Secondly, **this argument needs to be an array**. So in order to use sum, we need to provide it with _one_ array:

```dataview
LIST sum
FROM "10 Example Data/dailys"
WHERE paid
FLATTEN sum(paid) as sum
```

Huh, that doesn't give us an error anymore, but an improvable output. You want to know how to get a real sum? Head over to [[Mark all days in a calendar where you spent a certain amount of money#^8d9d50|"When using expenses in form of 99 $"]].