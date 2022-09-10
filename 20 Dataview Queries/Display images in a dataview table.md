---
description: display and resize images in dataview tables.
test-internal: "![[Bar Chart Category Series.png|500]]"
test-internal2: "[[Bar Chart Series Category Value 2.png]]"
topics:
  - images in tables
---
#dv/table #dv/from #dv/where #dv/embed #dv/meta #dv/link 

# Display images in a dataview table
> [!tip] Tip - Setting image size
> When returning an embeded image link in a dataview query, dataview will interpret an numeric display name alias as an image size. For example:
> - `[anyName](image-link)` will display the image at it natural largest size. 
> - `[anyname|50](image-link)` will display the image at a size of 50.
>
> **Note:** This `[]()` format only works for external images, and for internal images where you specify the full hard-drive path to the image file. For relative internal links, see [[#Basic - Internal Images]].

## Basic - External Images
**Link to a online image file saved as YAML**
``` YAML
---
Cover-Img: "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546512443i/43451211.jpg"
---
```

``` dataview
TABLE author as "Author", genres as "Genres", 
	  "![anyName|50](" + cover-img + ")" AS "Cover"
FROM "10 Example Data/books"
```

## Basic - Internal Images
> [!warning] Warning - Internal Image Links
> Internal links are usually stored as relative paths within the vault, making the previous `[]()` approach impractical for sizing internal images (because it requires the full hard-drive path to the image). 
>
> This means a different approach must be used for internal links. Below is one possible (simple) method, although this method reduces flexibilty by hard-coding the size of the image into the metadata field itself.  An alternative approach is outlined further below in [[#Internal Images - meta path approach]]. 

``` YAML
---
cover-img: "![[Some Internal Image.jpg|500]]"
---
```
``` dataview
TABLE test-internal AS ""
FROM ""
WHERE file.name = this.file.name
```


## Variations
### Internal Images - using the meta path approach
> [!warning] Warning - Internal Image Links
> Because internal links are stored as relative paths within the vault, it is impractical to use the `[]()` approach; and likewise it can be limiting to hard-code the embed information in the image link itself. 
> 
> To avoid this, an embeded link to an internal resource can be reverse enginered by using `meta(...).path` as follows:
> ` embed(link(meta(cover-img).path, "50"))`

``` YAML
---
cover-img: "[[Some Internal Image.jpg]]"
---
```

``` dataview
TABLE embed(link(meta(test-internal2).path, "500")) AS ""
FROM ""
WHERE file.name = this.file.name

```


### Mixed Images
> [!help] Help - I have a mixture of image sources!
> The code below combines the most flexible two methods above; allowing both internal and external images to be handled within the same query. 
> 
> The code is not pretty - so only use this approach if you know you will encounter mixed image sources. And if you find a cleaner method - let us know! 

``` YAML
---
cover-img: "[[Some Internal Image.jpg]]"

# OR

cover-img: "https://images.com/my-cool-external-image.jpg"
---
```

``` dataview
TABLE author, genres, EmbededCoverImg as ""
FROM "10 Example Data/books"
FLATTEN choice(typeof(cover-img)="link",
	embed(link(meta(
		choice(
			typeof(cover-img)="link", 
				cover-img, this.file.link
		)
	).path, "50")), "![anyName|50](" + cover-img + ")") AS EmbededCoverImg
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