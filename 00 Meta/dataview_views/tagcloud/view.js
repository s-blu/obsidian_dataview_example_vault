dv.container.className += ' tagcloud';

const uniqueValues = {};
input.values.forEach(val => {
  if (uniqueValues[val]) {
    uniqueValues[val]++;
  } else {
    uniqueValues[val] = 1;
  }
});

const quantities = Array.from(new Set(Object.values(uniqueValues).sort((a, b) => b - a)));
const sizeClassMap = {
  small: 1,
  medium: 2,
  big: 3,
};

if (quantities.length > 3) {
  const third = Math.floor(quantities.length / 3);
  sizeClassMap.small = quantities[quantities.length - third];
  sizeClassMap.medium = quantities[third * 2];
  sizeClassMap.big = quantities[third];
}

Object.keys(uniqueValues).forEach(t => {
  const sizeClass =
    uniqueValues[t] <= sizeClassMap.small ? 'small' : uniqueValues[t] <= sizeClassMap.medium ? 'medium' : 'big';
  dv.span(t, { cls: 'cloud-item ' + sizeClass });
});
