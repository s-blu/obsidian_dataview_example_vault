---
description: Show tv shows after current status in multiple tables switchable via button
topics:
  - show or hide queries
---
#dv/dataviewjs #dvjs/el #dvjs/pages #dvjs/where #dvjs/header #dvjs/table #dvjs/map #dvjs/container 

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
	dv.table(
	['Title', 'Rating', 'Runtime', 'Seasons', 'Episodes'], 
	pages.map(page => [page.file.link, page.rating, page.runtime, page.seasons, page.episodes]))
}

const removeTable = () => {
	this.container.lastChild.remove()
	this.container.lastChild.remove()
}

buttons.forEach(button => createButton(button))

renderTable('Watching')
```

## Variants

### Display amount of watched episodes

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
	
	dv.table(['Title', 'Rating', 'Runtime', 'Seasons', 'Ep watched/total'], pages.map(page => {
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

### Render other views/different ones per tab

```dataviewjs
const views = ['Table', 'List', 'Tasks']

const changeView = (viewName) => {
    removeView()

    if (viewName == 'Table') {
        dv.header('2', 'Some table')
        dv.table(['File', 'Day'], dv.pages('"10 Example Data/dailys"').limit(7).map(p => [p.file.link, p.day]))
    }
    if (viewName == 'List') {
        dv.list(dv.pages('"10 Example Data/dailys"').limit(7).file.name)
    }
    if (viewName == 'Tasks') {
        dv.taskList(dv.page("10 Example Data/projects/project_2").file.tasks)
    }
}

const createButtons = () => {
    const buttonContainer = dv.el('div', '', {cls: 'tabButtons'})
    
    views.forEach(view => {
        const button = dv.el('button', view)

        button.addEventListener('click', (event) => {
            event.preventDefault()
            changeView(view)
        })

        buttonContainer.append(button)
        
    })
}

const removeView = () => {
    Array.from(this.container.children).forEach(el => {
        if(!el.classList.contains('tabButtons')) {
            el.remove()
        }
    })
}

createButtons()
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