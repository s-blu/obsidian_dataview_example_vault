---
description: Query a folder structure with the help of meta files and display the per ID interconnected information in a table 
topics:
  - querying folder infos
---
 #dv/TABLE #dv/FROM #dv/FLATTEN #dv/groupby #dv/split #dv/length #dv/WHERE #dv/link #dv/filter #dv/dataviewjs #dvjs/pages #dvjs/array #dvjs/table

> [!hint] Contributed by [mnvwvnm and dbarenholz#2331](https://discord.com/channels/686053708261228577/1014259487445622855/1018526357006860328)

# Query meta files to construct information out of a folder structure

## Basic 

**If language info is redundant saved in the meta file**
```dataview
TABLE rows.lang, rows.Title AS Title
FROM "10 Example Data/Folder Structure and Meta Files"
WHERE file.name = "meta"
FLATTEN split(file.folder, "/")[length(split(file.folder, "/")) - 1] AS Title
GROUP BY id
```

**If language info should be extracted from path**

> [!attention] Vulnerable to changes of folder structure
> Extracting the language from the folder path requires to know the exact position of the language folder - in our case, it's the **third layer** (First: 10 Example Data, Second: Folder Structure and Meta Files). If this is to change, the query won't show the correct result anymore.

```dataview
TABLE rows.Language AS Language, rows.Title AS Title
FROM "10 Example Data/Folder Structure and Meta Files"
WHERE file.name = "meta"
FLATTEN split(file.folder, "/")[length(split(file.folder, "/")) - 1] AS Title
FLATTEN split(file.folder, "/")[2] AS Language
GROUP BY id
```

## Variants

### Add link to meta file while keeping ID information

```dataview
TABLE WITHOUT ID link, rows.lang, rows.Title AS Title
FROM "10 Example Data/Folder Structure and Meta Files"
WHERE file.name = "meta"
FLATTEN split(file.folder, "/")[length(split(file.folder, "/")) - 1] AS Title
GROUP BY id
FLATTEN link(rows.file[0].path, id) AS link
```

### Beautify language information out of meta file

```dataview
TABLE rows.Language AS Language, rows.Title AS Title
FROM "10 Example Data/Folder Structure and Meta Files"
WHERE file.name = "meta"
FLATTEN split(file.folder, "/")[length(split(file.folder, "/")) - 1] AS Title
FLATTEN ((x) => { EN: "English", FR: "French", DE: "German" }[x])(lang) AS Language
GROUP BY id
```

### Use languages as columns

```dataview
TABLE WITHOUT ID filter(rows, (r) => r.lang = "FR").Title AS French, filter(rows, (r) => r.lang = "EN").Title AS English, filter(rows, (r) => r.lang = "DE").Title AS German
FROM "10 Example Data/Folder Structure and Meta Files"
WHERE file.name = "meta"
FLATTEN split(file.folder, "/")[length(split(file.folder, "/")) - 1] AS Title
GROUP BY id
```

### Javascript solution that automatically adds new languages when available in folder structure

> [!attention] Vulnerable to changes of folder structure
> Extracting the language from the folder path requires to know the exact position of the language folder - in our case, it's the **third layer** (First: 10 Example Data, Second: Folder Structure and Meta Files). If this is to change, the query won't show the correct result anymore.

```dataviewjs
// Grab the folder
// If you type it manually it should be a string: "folder"
const folder = "10 Example Data/Folder Structure and Meta Files"
// Grab all pages from the desired folder
const allPages = dv.pages(`"${folder}"`)

// Get all languages from there into a set, and then as array.
// This will work for _any_ number of languages
let languages = new Set()
allPages.forEach((p) => {
	const lang = p.file.folder.split("/")[2]
	if (lang) {
		languages.add(lang)
	}
})
languages = dv.array(Array.from(languages))


// TODO: Define your language mapping here!
// The code uses the folder names for displaying, but I need to be able to match
// What's in the meta file to the folder name.
const langMap = {
	'EN': "English", 
	'DE': "German",
	'FR': "French"
}


// The headers of the table are the different languages
const headers = languages

// Keep data array with following information
/**
[
	{
		id: book-id,
		titles: [
			{ 
				lang: language-code, 
				title: book-title
			}
		]
	}
]
**/
let data = []

allPages.forEach((p) => {
	// Grab the title, language, and ID
	const title = p.file.folder.split("/")[p.file.folder.split("/").length - 1]
	const lang = p.lang
	const id = p.id

	// Add everything to "data" in a smart way
	if (lang && id && title) {
		const IDs = data.map(e => e.id)
		if (IDs.contains(id)) {
			console.log(`Data has id: ${id} at index: ${IDs.indexOf(id)}`)

			const toAdd = {lang: lang, title: title}
			data[IDs.indexOf(id)].titles.push(toAdd)

		} else {
			console.log(`Data has no ID: ${id}; creating new entry`)
			const newEntry = {
				id: id, 
				titles: [ { lang: lang, title: title } ]
			}
			data.push(newEntry)
		}	
	}
})

// Create table elements from the data we saved above
const elems = data
	// Get to the titles
	.map( (dataEntry) => { return dataEntry.titles })
	.map( (titleEntry) => {
		// Build a single table row
		let items = []
		
		// Loop through all titles & langs
		// making sure that entries are in the correct column
		titleEntry.forEach((title) => {
			languages.forEach((lang) => {
				if (lang == langMap[title.lang]) {
					// The title should be placed in the row at this position
					items.push(title.title)
				}
			})
		})
		return items
	})


// Make the actual table
dv.table(headers, elems)
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




