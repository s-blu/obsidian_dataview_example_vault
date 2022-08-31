# TODO create page/
# TODO copy 00 - 30 to page/
# TODO v2: replace callout syntax to work with adminition plugin

import shutil
from pathlib import Path

# TODO remove old pages dir first
shutil.rmtree('publish/pages')
# Path('publish/pages').mkdir()
dirsToCopy = ['00 Meta', '10 Example Data',
              '20 Dataview Queries', '30 Dataview Resources']

for dir in dirsToCopy:
    shutil.copytree(f'{dir}', f'publish/pages/{dir}')

shutil.copy('README.md', 'publish/pages/index.md')
