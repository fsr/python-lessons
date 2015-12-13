---
title: Dear regex, Merry Christmas!
number: 19
lesson: 10
status: drafty
authors: felixw
---

Ho ho ho, Christmas is coming! So today, we wanna write a script that automatizes the process of reading and analyzing children's christmas wishes.

### Step 1 - The Data.

The whole world is getting more and more digital. Some christmas elf converted all the children's letters to a digital format, saved them as a __JSON__ file and uploaded them.
First of all, your script should get the [christmas wishes](../misc/christmas.json) from the web, using the module _urllib_ or _requests_.[^urllib]

[^urllib]:
    TODO

Then, load the data, using the `json` module[^using] to have the data in a python-readable format. Now, analyze the the data you got. Does it follow a pattern?

### Step 2 - Sort out the Spam.

Now there are some kiddies who were not able to write a good wish letter.


### Step 3 - `He's gonna find out who's naughty and nice...`

Find out, who was naughty and who was nice.

### Step 4 - What are those children's wishes?

What do those kiddies wish for christmas?

They follow a pattern. (start with a `- `)

### Step 5 - Results for Santa!

Gather all your results and print them out in a nicely readable format, like:

```
Name von Kind 1: unartig/keine Wünsche
Name von Kind 2: Wünsche
...
```

Note that children that didn't write a correct wishlist are naughty in Santa's eyes, too!
