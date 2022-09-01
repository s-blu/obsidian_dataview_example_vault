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
shutil.copytree(f'.publish/assets', f'{pagesDir}/assets')

for (dirpath, dirnames, filenames) in os.walk(pagesDir):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        if ".md" not in filepath:
            continue
        try:
            with open(filepath, 'r') as file:
                filedata = file.read()

                # Remove navigation queries from bottom of file
                filedata = re.sub(
                    r"---\s(%% === end of query page === %%)(.+)", '', filedata, flags=re.DOTALL)

                # Change Callout syntax to admonition syntax
                filedata = re.sub(r"> \[\!(.+?)\][-+]? (.+)",
                                  r'!!! \1 "\2"', filedata)
                # Remove lines that just contain a "> " if there's another "> something" following, since empty lines break the admonition syntax
                filedata = re.sub(r">\s> (.+)", r'    \1', filedata)
                # TODO this also converts standard cite blocks, would need to check if I have a match with the first one before this
                filedata = re.sub(r"> (.+)", r'    \1', filedata)
                # escape hashes from tags so they don't get rendered as h1
                filedata = re.sub(r"(#)([^#\s]+)", r'\\#\2', filedata)
                # extract description from frontmatter and replace frontmatter with it. Isn't the fanciest thing to do, need to think of something better.
                filedata = re.sub(
                    r"^\s*---\s*(description: .+)[\S\s]*?---", r'_\1_\n', filedata)

                with open(filepath, 'w') as file:
                    file.write(filedata)
        except:
            print(
                "WARN: Could not read file for replacing callout syntax, skipping: " + filepath)
