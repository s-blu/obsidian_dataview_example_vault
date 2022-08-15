# Topic Cloud

Each query has one or more **topics**, grouping queries with simliar goals together. Wonder what's available? Wonder no more!

```dataviewjs
await dv.view("00 Meta/dataview_views/tagcloud", {values: dv.pages('"20 Dataview Queries"').where(p => p.topics).topics})
```

> [!info] Tagcloud query
> You want this fancy tag cloud for your own data? Head over to [[Display meta data values as a tag cloud]]