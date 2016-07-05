---
title: We want to edit!
number: 21
lesson: 12
status: drafty
authors: [felix, felixw]
---

Vim, Nano and emacs are console editors. But what if we want to build our own? Here it comes!

# Build the frame

First we have to create a screen with curses so we can build our CLI around it.


# The editor itself

In order to have an editor, we have to build one. Maybe with a nice frame around it?[^textpad]

[^textpad]:
    It is time for `curses.textpad`!

# Where?!

The editor is working but it is not useful if you can not save the file...
Add an open function which opens (or creates) a file to write the data in.

# Save it!

Don't forget to save the file!

# Make the creator an editor

For now we only can create new texts that overwrite the old ones...
Time to load the old text![^load]

[^load]:
    In order to load old text you simply have to use `curses.addstr(text)`
