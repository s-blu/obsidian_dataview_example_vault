---
description: Display random images from a path in vault
---
#dv/dataviewjs 

# Display random images from a path

## Basic 

```dataviewjs
const amountOfImages = 3; 
const pathToImageFolder = '00 Meta/attachments' 
const imageFiles = app.vault.getFiles().filter(file => file.extension !== 'md' && file.parent.path === pathToImageFolder) 

dv.list(dv.array(imageFiles)
		.sort(() => 0.5 - Math.random())
		.limit(amountOfImages)
		.map(file => dv.func.embed(dv.fileLink(file.path))))
```