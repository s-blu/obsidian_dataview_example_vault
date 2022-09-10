---
description: Overview of handling various types of frontmatter fields, including tricks and traps.
topics:
  - basics

emptyValue:
Bool: false
Numeric: 10.5
StringNumeric: "10.5"

StringWithQuotes: "Test"
StringNoQuotes: Test
StringEscapting: "Basic 'quotes' inside \"quotes\""
StringHTML: "<B>That</B> text is coloured<BR><span style='color:green;'>green</span>"
StringMultiline:
  Block starts indended on a new line, and 
  each new line starts indended by two spaces.
  String continues until intented lines stop.
StringMultiWithBreaks: |
  Block starts with a pipe symbol, and 
  each new line starts indended by two spaces.
  String continues until intented lines stop.

Date: 2022-05-06
DateTime: 2022-05-06T10:15
Duration: 1 day

Link: "[[Dataview Documentation]]"

FlatArray: ["A", "B", "C"]
BulletArray: 
  - "A"
  - "B"
  - "C"

KeyedObject: {name: "My Object", value: 7.5, occured: 2022-01-09}
NestedObject: [
	{name: "nest1", color: "FF0000"},
	{name: "nest2", color: "00FF00"},
	{name: "next3", color: "0000FF"}
]
---
# Working with Frontmatter
> [!bug] This page is a work in progress. 

> [!tldr] Navigation
> [[#Numbers]] | [[#Strings]] | [[#Links]] | [[#Dates]] | [[#Arrays]] | [[#Objects]]

---

## Numbers & Logic
``` dataview
TABLE WITHOUT ID EmptyValue, Bool, Numeric, StringNumeric
FROM ""
WHERE file.name = this.file.name
```

---

## Strings
#### Basic
``` dataview
TABLE WITHOUT ID StringWithQuotes as "String in Quotes", StringNoQuotes as "String no Quotes", StringEscapting as "String Escaping", StringHTML as "String with HTML"
FROM ""
WHERE file.name = this.file.name
```

#### Multiline
``` dataview
TABLE WITHOUT ID StringMultiline, StringMultiWithBreaks
FROM ""
WHERE file.name = this.file.name
```

> [!tip] Tips for Working with Strings
> - 

> [!warning] Traps for Working with Strings
> - 

---

## Links
``` dataview
TABLE WITHOUT ID Link, Link.file.cday
FROM ""
WHERE file.name = this.file.name
```

---

## Dates
``` dataview
TABLE WITHOUT ID Date, DateTime, Duration, Date + Duration as "Date + Duration", dateformat(Date, "yyyy-MM") as "Formatted Date"
FROM ""
WHERE file.name = this.file.name
```

---

## Arrays
``` dataview
TABLE WITHOUT ID FlatArray, BulletArray
FROM ""
WHERE file.name = this.file.name
```
- If field is an array (like in your case), then contains is looking for an _element_ that matches exactly. So if you had `field:: [[abc]], [[def]], a` then it would match. If field is a string (an array of characters)... it would still be looking for an _element_ it's just that in that case elements are individual characters.  A simple way around it would be to do `=contains(join(this.field), "a")` which turns the array into a string, and then does a character search for any a's.


---

## Objects
#### Basics
``` dataview
TABLE WITHOUT ID KeyedObject, NestedObject
FROM ""
WHERE file.name = this.file.name
```

#### Looking inside
``` dataview
TABLE WITHOUT ID KeyedObject.name, NestedObject[0].color, "<div style='background-color:#" + NestedObject[0].color + ";'> </div>" as  "HTML Color"
FROM ""
WHERE file.name = this.file.name
```


#### Flattening objects
``` dataview
TABLE WITHOUT ID NObjects.name, NObjects.color, "<div style='background-color:#" + NObjects.color + ";'> </div>" as  "HTML Color"
FROM ""
WHERE file.name = this.file.name
FLATTEN NestedObject as NObjects
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