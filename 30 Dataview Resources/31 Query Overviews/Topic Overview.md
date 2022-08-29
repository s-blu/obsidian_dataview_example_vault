# Topic Overview

Each query has one or more **topics**, grouping queries with similar goals together. Wonder what's available? Wonder no more!

```dataviewjs
await dv.view("00 Meta/dataview_views/tagcloud", {values: dv.pages('"20 Dataview Queries"').where(p => p.topics).topics})
```

## Topic List

```dataview
TABLE WITHOUT ID t as "Topic", count, rows.file.link AS "pages"
FROM "20 Dataview Queries"
WHERE topics
FLATTEN topics AS t
GROUP BY t
FLATTEN length(rows.file.link) as count
SORT count DESC, t ASC
```

> [!info] Used queries
> You want these fancy queries for your own data? Find the [[Display meta data values as a tag cloud|tag cloud here]] and [[List pages that share a meta data value with the current page|the list here]].