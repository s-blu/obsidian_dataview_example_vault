---
description: Show tv shows after current status in multiple tables switchable via button
---
#dv/dataviewjs

# Render multiple tables with tab-like buttons

## Basic 

```dataviewjs
const createButton = (name) => {
	const btn = dv.el('button', name)
	btn.addEventListener('click', (event) => {
		event.preventDefault()
		removeTable()
		renderTable(name)
	})
	
	return btn
}

const buttons = ['Watching', 'Going to watch', 'Watched all', 'Stopped watching']


const renderTable = (name) => {
	const pages = dv.pages('"10 Example Data/shows"').where(page => page.status == name)
		
	dv.header(2, name)
	
	const tabel = dv.table(['Title', 'Rating', 'Runtime', 'Seasons', 'Episodes'], pages.map(page => [page.file.link, page.rating, page.runtime, page.seasons, page.episodes]))
}

const removeTable = () => {
	this.container.lastChild.remove()
	this.container.lastChild.remove()
}

buttons.forEach(button => createButton(button))

renderTable('Watching')
```

## Variants

Display amount of watched episodes

```dataviewjs
const createButton = (name) => {
	const btn = dv.el('button', name)
	btn.addEventListener('click', (event) => {
		event.preventDefault()
		removeTable()
		renderTable(name)
	})
	
	return btn
}

const buttons = ['Watching', 'Going to watch', 'Watched all', 'Stopped watching']


const renderTable = (name) => {
	const pages = dv.pages('"10 Example Data/shows"').where(page => page.status == name)
	
	dv.header(2, name)
	
	const tabel = dv.table(['Title', 'Rating', 'Runtime', 'Seasons', 'Ep watched/total'], pages.map(page => {
	let watchedEp = 0
	const totalEp = page.episodes
	
	page.file.tasks.values.forEach(el => {
		if(el.checked) {
			watchedEp += 1
		}
	})
	return [page.file.link, page.rating, page.runtime, page.seasons, `${watchedEp}/${totalEp}`]
	}))	
}

const removeTable = () => {
	this.container.lastChild.remove()
	this.container.lastChild.remove()
}

buttons.forEach(button => createButton(button))

renderTable('Watching')
```