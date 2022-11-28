// requiring or importing the lib did not work, thus we call it directly from within the same file
const Colcade = factory();

const yearAndWeek = ["2022", "2"] // ATTENTION! replace this line with: const yearAndWeek = input.current.file.name.split('-W')
const pages = dv
  .pages(input.dailyNotesSearchQuery)
  .where(p => p.file.day && p.file.day.year == yearAndWeek[0] && p.file.day.weekNumber == yearAndWeek[1])
  .sort(p => p.file.name);
dv.container.className += ' imagegrid';

// render column elements for colcade. Styling is optimised for three columns. 
for (let i = 0; i < 3; i++) {
  dv.el('div', '', { cls: 'grid-col' });
}

//render images
dv.list(pages[input.metadatafield]);
// move the rendered images into the container so colcade can handle them (doesn't work if they are nested)
dv.container.querySelectorAll('ul li img').forEach(el => {
  el.className = 'grid-item';
  dv.container.appendChild(el);
});

new Colcade(dv.container, {
  columns: '.grid-col',
  items: '.grid-item',
});

/* ==== COLCADE LIBRAY, MIT LICENSED, SOURCE: https://github.com/desandro/colcade ===== */
/* ATTENTION: This code is minimized in functionality to only yield code we need for the specific use case */

/*!
 * Colcade v0.2.0
 * Lightweight masonry layout
 * by David DeSandro
 * MIT license
 */
function factory() {
  // -------------------------- Colcade -------------------------- //

  function Colcade(element, options) {
    element = getQueryElement(element);

    // do not initialize twice on same element
    if (element && element.colcadeGUID) {
      var instance = instances[element.colcadeGUID];
      instance.option(options);
      return instance;
    }

    this.element = element;
    // options
    this.options = {};
    this.option(options);
    // kick things off
    this.create();
  }

  var proto = Colcade.prototype;

  proto.option = function (options) {
    this.options = extend(this.options, options);
  };

  // globally unique identifiers
  var GUID = 0;
  // internal store of all Colcade intances
  var instances = {};

  proto.create = function () {
    // add guid for Colcade.data
    var guid = (this.guid = ++GUID);
    this.element.colcadeGUID = guid;
    instances[guid] = this; // associate via id
    // update initial properties & layout
    this.reload();
  };

  // update properties and do layout
  proto.reload = function () {
    this.updateColumns();
    this.updateItems();
    this.layout();
  };

  proto.updateColumns = function () {
    this.columns = querySelect(this.options.columns, this.element);
  };

  proto.updateItems = function () {
    this.items = querySelect(this.options.items, this.element);
  };

  proto.getActiveColumns = function () {
    return this.columns.filter(function (column) {
      var style = getComputedStyle(column);
      return style.display != 'none';
    });
  };

  // ----- layout ----- //

  // public, updates activeColumns
  proto.layout = function () {
    this.activeColumns = this.getActiveColumns();
    this._layout();
  };

  // private, does not update activeColumns
  proto._layout = function () {
    // reset column heights
    this.columnHeights = this.activeColumns.map(function () {
      return 0;
    });
    // layout all items
    this.layoutItems(this.items);
  };

  proto.layoutItems = function (items) {
    items.forEach(this.layoutItem, this);
  };

  proto.layoutItem = function (item) {
    // layout item by appending to column
    var minHeight = Math.min.apply(Math, this.columnHeights);
    var index = this.columnHeights.indexOf(minHeight);
    this.activeColumns[index].appendChild(item);
    // at least 1px, if item hasn't loaded
    // Not exactly accurate, but it's cool
    this.columnHeights[index] += item.offsetHeight || 1;
  };

  // -------------------------- HTML init -------------------------- //

  docReady(function () {
    var dataElems = querySelect('[data-colcade]');
    dataElems.forEach(htmlInit);
  });

  function htmlInit(elem) {
    // convert attribute "foo: bar, qux: baz" into object
    var attr = elem.getAttribute('data-colcade');
    var attrParts = attr.split(',');
    var options = {};
    attrParts.forEach(function (part) {
      var pair = part.split(':');
      var key = pair[0].trim();
      var value = pair[1].trim();
      options[key] = value;
    });

    new Colcade(elem, options);
  }

  Colcade.data = function (elem) {
    elem = getQueryElement(elem);
    var id = elem && elem.colcadeGUID;
    return id && instances[id];
  };

  // -------------------------- utils -------------------------- //

  function extend(a, b) {
    for (var prop in b) {
      a[prop] = b[prop];
    }
    return a;
  }

  // turn element or nodeList into an array
  function makeArray(obj) {
    var ary = [];
    if (Array.isArray(obj)) {
      // use object if already an array
      ary = obj;
    } else if (obj && typeof obj.length == 'number') {
      // convert nodeList to array
      for (var i = 0; i < obj.length; i++) {
        ary.push(obj[i]);
      }
    } else {
      // array of single index
      ary.push(obj);
    }
    return ary;
  }

  // get array of elements
  function querySelect(selector, elem) {
    elem = elem || document;
    var elems = elem.querySelectorAll(selector);
    return makeArray(elems);
  }

  function getQueryElement(elem) {
    if (typeof elem == 'string') {
      elem = document.querySelector(elem);
    }
    return elem;
  }

  function docReady(onReady) {
    if (document.readyState == 'complete') {
      onReady();
      return;
    }
    document.addEventListener('DOMContentLoaded', onReady);
  }

  // -------------------------- end -------------------------- //

  return Colcade;
}
