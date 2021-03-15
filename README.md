# Weave
Experimental automation for personal journalling inspired by Twine 2, Infinilist and Roam - editors that utilize a graph structure for expanding on your content, instead of the traditional linear / heirarchical structure.

This is highly experimental and hacky result of a single evening of coding.

-- Edit -- I've recently tried out Obsidian. I highly encourage you to give it a go! Obsidian has already done what I was setting out to do with this little side-project. https://obsidian.md

# Notes on development so far
I used the open source repo for Twine 2 editor as a guide in this experiment. Anyone could do this.

So far I have a link parser that scans for [[this syntax]] for any text you give it. I've also made a rudimentary node builder that creates a flat file structure in a new directory in your home folder, and adds in a new node for the day you run the app - your "Journal" node, with todays date. You can also pass it arbitrary text with [[links]] and it will create nodes for each [[link name]] and give it a markdown extension in that directory.

##### Directory structure for above examples of links
```
data/"December 16, 2020.md"
data/"this syntax.md"
data/"links.md"
data/"link name.md"
```

##### Structure of a node file:
```
Node Name
comma,seperated,list,of,tags
Hello world! This is your entry.
You can put whatever text you like here.
Good luck!
```
The first line of the file is the reference "name" just because I imagine it best to abstract the file name, though we'll see.
The second line is a comma separated list of "tags"
the third line begins all the data of the node, whatever that may be.

# What's next?
This little experiment will probably not go any further than this, and I mostly used the twine 2 source as a guide, so anyone could do it.
The biggest point of friction at the moment is that you would need to have a custom extension / plugin for your favourite editor to do the following:
* Run the link parser and highlight links as such.
* Open a link to a node file in a new tab when you click on it or otherwise semantically attempt to "enter" the link.

I'll might try to make such an extension for vim.]

But ye, when I was thinking about how one would make this app, most of the benefit could be achieved quite simply with something that checks for link syntax and creates nodes imperitavely. The searching could be done by the native searching support in your favourite editor, or with the simple addition of a fuzzy search extension/plugin.

The "back linking" feature of Roam would simply be a case of running the link parser on all the nodes in the graph. You don't need to keep a list of edges, you just need a node at a destination. So the main thing that would take this from an evening project to a more elaborate one is making some basic abstraction layer for nodes and their file name. Again this featured could be ignore and similar effect achieved imperatively by sticking to some standard naming convention.

## Author
Darren Kearney - @darrencearnaigh

## References
Twine 2 - https://twinery.org
Roam - https://roamresearch.com
