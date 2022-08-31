# TODO v2: replace callout syntax to work with adminition plugin

import shutil
from pathlib import Path

if Path('publish/pages').is_dir():
    shutil.rmtree('publish/pages')
# Path('publish/pages').mkdir()
dirsToCopy = ['00 Meta', '10 Example Data',
              '20 Dataview Queries', '30 Dataview Resources']

for dir in dirsToCopy:
    shutil.copytree(f'{dir}', f'publish/pages/{dir}')

shutil.copy('README.md', 'publish/pages/index.md')
