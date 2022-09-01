import shutil
import os
import re
from pathlib import Path

pagesDir = ".publish/pages"

if Path(pagesDir).is_dir():
    shutil.rmtree(pagesDir)
dirsToCopy = ['00 Meta', '10 Example Data',
              '20 Dataview Queries', '30 Dataview Resources']

for dir in dirsToCopy:
    shutil.copytree(f'{dir}', f'{pagesDir}/{dir}')

shutil.copy('README.md', f'{pagesDir}/index.md')

for (dirpath, dirnames, filenames) in os.walk(pagesDir):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        if ".md" not in filepath:
            continue
        try:
            with open(filepath, 'r') as file:
                filedata = file.read()
                filedata = re.sub(r"> \[\!(.+?)\][-+]? (.+)",
                                  r'!!! \1 "\2"', filedata)
                # TODO this also converts standard cite blocks, would need to check if I have a match with the first one before this
                filedata = re.sub(r"> (.+)", r'    \1', filedata)

                with open(filepath, 'w') as file:
                    file.write(filedata)
        except:
            print(
                "WARN: Could not read file for replacing callout syntax, skipping: " + filepath)
