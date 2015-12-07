---
title: Ping-Pong on the client side of the internet
status: drafty
number: 17
authors: [justus, felixw]
---

### Implementing your own version of `ping`

Take a url as input.

In a loop try to establish a connection to a website every n seconds _(30 is recommended)_. In the world of web pages, you always want to get `Status: 200` back when reaching out to a server.
If you get Status 200 back terminate, otherwise print the status code and keep going. Note that you can terminate your script with `Ctrl + C` anytime.

To try your script on a not working webpage, you can use something like `http://whbfuwvfbiuwe.github.com`.
