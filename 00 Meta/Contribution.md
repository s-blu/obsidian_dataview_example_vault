# How to contribute

First of all, thanks for considering sharing your knowledge! For adding a query to the vault, there are two things to do: First, **add the query** with fitting test data so it produces results and secondly, **share the query** so it'll become part of the example vault.

## Get a local copy

First of all, you need to get yourself a local copy of the example vault. There are two ways of doing this.

1. Get a static local copy. Follow the [[README#Usage]] explanation for that
2. Get a copy via Github - this is more technical, but makes it possible to update the vault to the newest state automatically and makes sharing your contribution easier.

### Get the example vault via GitHub

You'll need a GitHub Account to follow these steps. If you're not git-savvy, it's probably easier for you to use the [GitHub Desktop](https://desktop.github.com/) application for the following steps.

1. [Create a fork and clone it](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop#forking-a-repository) of the [example vault](https://github.com/s-blu/obsidian_dataview_example_vault) . Now you should have a local copy you can work with.
3. Make your changes like described below!

## Add a query

When you want to add a brand new query, please do the following:

1. Check via search if there's maybe already a file with the same goal. Then it might be best to add your query as a **Variant** of this existing file. A Variant of a query does, in the end, produces the same or a very similar/enhanced result like the Basic query, but adds more convenient, better readability, better usability or similar. 
2. If you don't find anything, create a new file under folder "20 Dataview Queries"
3. Give it a descriptive name that describes the general goal of your query. Read the existing titles to get an idea.
4. Insert the provided **dataview query template** by hitting CTRL + T
5. Follow the checklist of the template 
6. If necessary, add test data for your query. See [[Contribution#Add test data]] for details
7. Done - good job! The second step is to [[Contribution#Share your contribution|share your contribution with us]]

## Add test data

Probably, your query will need some specific test data. You can either add new files or expand existing ones. Please keep these points in mind:

1. Do not delete or change existing test data, even it if looks broken. It could be that a query page needs these broken data sets to showcase how to handle such edge cases
2. Always add test data in a sub folder of `10 Example Data`, i.e. `10 Example Data/recipes`. You're free to create new ones for this. This makes querying easier. You can, of course, also add tags to do the querying. Still, it is easier for maintenance if you put the data in a sub folder
3. Please make sure your test data does not hurt anyone, doesn't contain personal data and is not illegal (i.e. Copyright infringement)

> [!tip] Script to generate semi-random test data
> There is a [python script](https://github.com/s-blu/obsidian_things/tree/main/example_data) around, that lets you generate test data with some random values based on one or more template files. Most of the data under 10 Example data/dailys and 10 Example Data/books were generated with it - maybe it's a good fit for you, too. More info on the script itself.

## Share your contribution

You've added a new query or enhanced the vault in some other way. Thanks a lot! When you created a fork via GitHub, please follow these steps.

### When you used a downloaded local copy

If you used a static copy of the vault, but still own a GitHub account, please proceed as follows:

1. Go to issues in the [dataview example vault repository](https://github.com/s-blu/obsidian_dataview_example_vault/issues) 
2. Hit "New Issue" on the right
3. Give the issue a name that reflect your changes, i.e. "Add query about (title of query file)"
4. Attach all files you've created or changed to the issue
5. Hit "Submit new issue"
6. We'll review your changed files and integrate them into the dataview example vault if everything is alright

**If you can't share your contribution via GitHub**, drop a message in the #dataview thread of the Obsidian Discord and somebody will take care of that for you. Mind though, it's easiest for the maintainers if you share your contribution via GitHub.

### When you've created a fork

1. [Push your changes to your fork](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/making-changes-in-a-branch/pushing-changes-to-github). Now, your contribution is available online, but not in the original example vault yet!
2. For that, you need to [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) against the original repository.
3. Wait for our review - we'll merge your changes if everything is alright and make your contribution available for everyone!