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

To get started, we are going to need some recipients. Since using leaked mail addresses found on darknet marketplaces is kind of illegal and might cause us some stress, let's just use a [list](https://fsr.github.io/python-lessons/misc/recipients.json) of "voluntary recipients" from our web server.


## Gather Recipients

Let's assume `https://fsr.github.io/python-lessons/misc/recipients.json` contains a well maintained list of mailing list subscribers that thirst for your mail.

Get the recipient list from the web server[^urllib] and parse the addresses. As you can see from taking a look into the file, it's a __JSON__. So let's use the `json` module for the parsing.

[^urllib]:
    There was this module... `urllib.request`, do you remember? ;)

## Content

Before we can send _anything_, we need that anything. We need content. Write some content in a plain text file. This will be the text we will send to our recipients afterwards.  
As we would be very pleased to get some feedback for this course, feel free to write some lines about how you liked this course! Otherwise, you can be creative and write what ever you want.

After you've written a small piece of text, read it from the file. Note that you can use `f.read()` here instead of `f.readlines()`:

{% highlight python %}
with open(filename) as f:
    content = f.read()

print(content)  # contains a single multiline string
{% endhighlight %}

## Build the Mail!

Even though we haven't configured the mail account yet, let's build the mail object itself and prepare it for sending.

Initialize the `MIMEText` object with the content you already read from the file and add more information regarding sender and recipient(s) of the mail:

{% highlight python %}
# initialize the message object

message['From'] = 'Your Name <mail@example.com>'
message['To'] = 'Poor Guy <alwaysgetsspammed@badluckbri.an>'
# you might set more inforamtion like the subject and Cc/Bcc
{% endhighlight %}

## Adjust the settings

Now comes the part where we make a connection to the server and authenticate to send the mail we just built.
Use the context manager to open a `SMTP` connection and log in with the user data we provide you with. Don't forget to enable starttls before starting!

After the login was successfull, sou can use `smtplib.send_message(...)` to send your own mail to the world.

## Know your Errors

Don't forget the error handling! Try to catch every error that could occur to make your script run as fast as possible!
