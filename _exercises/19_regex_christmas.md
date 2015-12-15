---
title: Dear regex, Merry Christmas!
number: 19
lesson: 10
status: reviewed
authors: [felixw, felix]
---

Ho ho ho, Christmas is coming! So today, we wanna write a script that automatizes the process of reading and analyzing german children's christmas wishes.

### Step 1 - The Data.

The whole world is getting more and more digital. Some christmas elf converted all the children's letters to a digital format, saved them as a __JSON__ file and uploaded them.
First of all, your script should get the [christmas wishes](../misc/christmas.json) from the web, using the module _urllib_ or _requests_.[^urllib]
The full URL is `http://fsr.github.io/python-lessons/misc/christmas.json`.

[^urllib]:
    Remember to `import urllib.request` and have a look at our last lesson regarding the URL library. Hint: use something like `urllib.request.urlopen()` with `.read().decode("UTF-8")` to get the data.

Then, parse the data, using the `json` module[^using] to have the data in a python-readable format. Now, analyze the the data you got. Does it follow a pattern?

[^using]:
    Have a look at the [docs](https://docs.python.org/3.5/library/json.html?highlight=json.loads) if you need a little refreshment in terms of _"How to read json data"_.

### Step 2 - Sort out the Spam.

Now there are some kiddies who were not able to write a good wish letter or just wanted to send Santa some spam mail.
Those letters can be easily recognized, since they are not starting with a _"Lieber Weihnachtsmann, ..."_.

Start to sort out the whishlists by saving names of those kids who were not able or willing to write a good letter in a new list for naughty children.
We will need those names for step 5.

### Step 3 - _"He know's if you've been bad or good..."_

Find out, who was naughty and who was nice. Or at least you check if the child was nice all the time.  
Check with an regex if the whishlist contains `'ich war immer lieb'` or `'ich war immer artig'`.

### Step 4 - What does Santa have to buy?

Santa doesn't want to read whole letters. He wants to get a list of items to buy for every _good_ child.[^dict]

[^dict]:
    So start to build a new dict with an entry for every good child.

The whishes follow a pattern (every new wish starts with a `- `).[^finditer]<sup>,</sup>[^groups]

[^finditer]:
    In the previous steps we only needed a single match. Here we should use `finditer` to get an iterable of all available match objects.

[^groups]:
    Do not forget: You can use groups to get the information out of them!

### Step 5 - Results for Santa!

Gather all your results and print them out in a nicely readable format, like:

```
Name von Kind 1: unartig/keine Wünsche
Name von Kind 2: Wünsche
...
```

Note that children that didn't write a correct wishlist are naughty in Santa's eyes, too!

Dump your generated list also as a text file that can be sent to Santa later.

### Done!

Merry Christmas!
