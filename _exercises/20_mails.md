---
title: Put the news into letters!
number: 20
lesson: 11
status: drafty
authors: [felixw, felix]
---

[...]

In this exercise we are going to write our own really small and dead simple implementation of a mailing list or group notification system using Python.
Our goal is to write a script that gathers some mail addresses from a predefined server and uses a text file as source for some kind of newsletter.

To get started, we are going to need some recipients. Since using leaked mail addresses found on darknet marketplaces is kind of illegal and might cause us some stress, let's just use a list of "voluntary recipients" from our web server.


## Gather Recipients

Let's assume `https://fsr.github.io/python-lessons/misc/recipients.json` contains a well maintained list of mailing list subscribers that thirst for your mail.

Get the recipient list from the web server[^urllib] and parse the addresses. As you can see from taking a look into the file, it's a __JSON__. So let's use the `json` module for the parsing.

[^urllib]:
    There was this module... `urllib.request`, do you remember? ;)

## Content

Before we can send _anything_, we need that anything. We need content. Write some content in a plain text file. This will be the text we will send to our recipients afterwards.  
As we would be very pleased to get some feedback for this course, feel free to write some lines about how you liked this course! Otherwise, you can be creative and write what ever you want.


## Build the Mail!

Do it!
