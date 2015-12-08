---
title: Dad? What's for breakfast?
number: 18
status: finished
authors: felixw
---

The [students union](https://studentenwerk-dresden.de) offers the meals from all of it's canteens via [OpenMensa](https://openmensa.org) in a machine-readable format for everyone.

We will now go for writing a script that get's us todays[^today] meals and prints them for us, nicely formatted.

[^today]:
    Today sounds like `import time`, doesn't it? ;)

### Getting started

At first, let us analyze  what we need to do. The OpenMensa delivers the meals via an URL adhering to the following scheme:

`http://openmensa.org/api/v2/canteens/$mensaID/days/$date/meals`

The $mensaID of the _alte Mensa_ is __79__. The date has to be formatted as _ISO-8601_ string (e.g. `2015-12-08`)[^formatting].

[^formatting]:
    This is equal to the output of `time.strftime("%Y-%m-%d")`.

Using this information, write a function that builds you the link for the meals being served today in the _Alte Mensa_ and return it. Then open the returned link in your web browser. What do you get?[^dirty]

[^dirty]:
    Now that's some dirty formatted JSON!

### Working with what we got

So it seems that calling this link get's us some weird and crappy-formatted JSON file.

Write now a function that gets the content of that file[^decoding] and reads the JSON[^json]. Analyze the contents you got.

[^decoding]:
    If you use `urllib.request.urlopen()`, note that this function returns a bytes object when using `read()` that needs to be decoded to _UTF-8_ using `object.decode("UTF-8")`

[^json]:
    To load data from a String instead of a file, use `json.loads()`.


### Details!

Looks like that data is just a list of dicts where every dict represents a separate meal. That makes working with it pretty easy!

So an example meal dict could look like this (with better formatting...):[^dictslists]

{% highlight json %}
[
    {
        "prices": {
            "others": null,
            "pupils": null,
            "employees": 4.29,
            "students": 2.6
        },
        "notes": [
            "Menü enthält Knoblauch"
        ],
        "category": "Angebote",
        "name": " Hähnchenbrust mit Tomaten-Joghurt-Dip, dazu glasierte Honigmöhren und Kräuter-Chilikartoffeln",
        "id": 1663748
    },
    ...
]
{% endhighlight %}

[^dictslists]:
    Remember that there are also dicts and lists inside of that dict!


So let's get to work with formatting everything.

Write a function that prints the meals you gathered to the command line, nicely formatted. It should at least display The name of the meal and the price.

You can pimp that by displaying the notes related to the meal.


### Data whore

To seal the deal save your formatted text to a `*.txt` file.
