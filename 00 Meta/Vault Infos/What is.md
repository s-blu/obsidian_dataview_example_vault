# What is

This note provides embedable callouts to explain certain functionality in-place in query pages.

> [!info] dv.view
> This query uses the [dv.view mechanism of dataview](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/#dvviewpath-input). Views allow you to to reuse complex javascript queries and to add css styling to them. You'll find used dataview view files under `00 Meta/dataview_views`.

^dv-view

> [!hint] New "ID" after grouping
> When grouping, your "first level" changes. Without grouping, the first level are the file links you get back from your `FROM/WHERE` statement, so they automatically get displayed if you give no additional information to the `LIST` or `TABLE` command. The file link is the ID of your results.
> After grouping though, your _groups_ become the first level, the ID of your rows. That means without adding an additional information you'll see the groups in your list or table instead of the file links. To still see the file names, you need to pass them as your additional information to display per `rows.file.link`. Find out more about this in [[How GROUP BY works]]

^new-id-after-grouping