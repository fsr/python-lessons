---
theme: black
title: Pythonn als Webclient
---

# urllib.request

---

> The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

## urlopen

... öffnet eine URL. (surprise)

    urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

**url** kann ein String sein, wie 'http://python.org' oder 'ftp://store.stuff.de', oder eine komplexere Anfrage in Form eines Request objects sein.  
**data** enthält Daten, die an den Server gesendet werden. Muss vom Typ `bytes` oder `bytearray` sein.

Bei URLs mit *http*-Requests wird ein [httplib.client.HTTPResponse](#httpresponse-class) Objekt zurück gegeben.
Bei ftp, file und data ein urllib.response.addinfourl Objekt.


## Request Klasse



## HTTPResponse Klasse
