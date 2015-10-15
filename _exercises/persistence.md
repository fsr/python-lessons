---
title: Be persistent - save your data!
status: drafty
authors: felixw
---

## (1) Using JSON

Write a script that imports the __text statistics__ script, counts the dummy text and exports the statistics you gathered, using JSON.[^jsondocs]

[^jsondocs]:
    See the [docs](https://docs.python.org/3/library/json.html) for more information.


## (2) Using pickle

In __More objects!__ you wrote a rudimentary contact manager. Now splice it with some persistence features.

You can read the documentation for the pickle module [here](https://docs.python.org/3/library/pickle.html).

### Step 2.1

Add a function `saveContacts()` which dumps your whole contact list to a file named "backup.pkl".

Call the function inside your *main* function, after you created some contacts.

Run the script and have an eye on the folder the script lives in. What happens during execution?


### Step 2.2

Now add a function `loadContacts()` that obviously should retrieve your contact list from the backup file.

To play it safe, import the function `isfile()` from the os.path package[^cheat] and check if the backup file exists before you try to load any contacts from a list. If the file is not existent, return from the function and print a message about this.  
Otherwise, load the contacts from the file.

[^cheat]:
    This is in python: `from os.path import isfile`.
