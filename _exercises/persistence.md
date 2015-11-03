---
title: Be persistent - save your data!
status: reviewed
authors: [felixw, felix]
number: 11
lesson: 4
---

## Statistics worth saving.

Write a script that imports the __text statistics__ script, counts the dummy text and exports the statistics you gathered, using JSON.[^jsondocs]

[^jsondocs]:
    See the [docs](https://docs.python.org/3/library/json.html) for more information on how to use JSON.


## Save some contacts.

### Step 1
In __More objects!__ you wrote a rudimentary contact manager. Time to create a little generator around it to automatically fill it with some dummy data.

Load [this](../misc/contactdata.json) (Rightclick -> Download Linked File) JSON file to get a list of first- and lastnames.  
Use the builtin module `random`[^random] to pick one element from those lists of names.  
The mail-address should be `firstname.lastname@python.course`.

### Step 2
Now write a script that generates about 20 contacts and dumps them via JSON.

Use randomly generated 12 digits long numbers for the phone numbers. The date of birth can be ignored. Use a hard coded value like `01.01.1859` for all generated contacts.

### Step 3
If there is already a JSON file, load it, add 3 more contacts and dump it again.

Test your script.

[^random]:
    You should initialize the random with `random.seed()` and get an `randint` in a certain range.
    Have a look into the [docs](https://docs.python.org/3/library/random.html) for further information.
