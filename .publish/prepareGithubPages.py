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
shutil.copy('.publish/tagindex.md', f'{pagesDir}/tagindex.md')


def moveTagsToFrontmatter(filedata):
    tags = re.findall(r"[\s]#(dv[js]*/[^\^\#\`\s]+)", filedata)
    if tags:
        tagFrontmatter = '---\ntags:\n'
        for tag in tags:
            tagFrontmatter += f'  - {tag}\n'
        tagFrontmatter += '---\n'
        filedata = re.sub(r"[\s]#([^\^\#\s]+)", r'', filedata)
        filedata = tagFrontmatter + filedata
    return filedata


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

                # extract description from frontmatter and replace frontmatter with it. Isn't the fanciest thing to do, need to think of something better.
                filedata = re.sub(
                    r"^\s*---\s*description: (.+)[\S\s]*?---", r'!!! info "\1"\n', filedata)

                # Add hint to Overview pages pointing to the tagindex
                if ("31 Query Overviews" in filepath):
                    filedata = '!!! warning "Overviews in Online Version"\n    The overview pages are not usable in online view. Please refer to the [[tagindex]].\n\n' + filedata

                # Add tags to frontmatter
                if ("20 Dataview Queries" in filepath):
                    filedata = moveTagsToFrontmatter(filedata)

                with open(filepath, 'w') as file:
                    file.write(filedata)
        except UnicodeDecodeError:
            print(
                "WARN: Could not read file for replacing callout syntax, skipping: " + filepath)
