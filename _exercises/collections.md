---
title: You'll need me soon enough - Collections
status: drafty
---

### `namedtuple`

(Download and) Open [this](/misc/clarkson.yml) file. Parse the contents and store it[^storing].

[^storing]:
    You can store the data either in a `dict`, though that'll make things a little harder in the future. Or a `list` of key-value pairs (`tuple`).

Rules for parsing:

- the key is on the left side
- the value on the right
- key and value are separated by a colon and a space (': ')

We'd like to use this data as configuration data. That's why we'd prefer to have non-changing keys and we'd like some more convenient/better looking access.

So we create a new `namedtuple` where the names of the fields are the keys from the file. As initial values we'd like the values from the file we read.

Finally parameterize your function such that it accepts an arbitrary filename and returns the appropriate namedtuple.
