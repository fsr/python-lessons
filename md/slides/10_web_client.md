---
title: Python als Webclient
---

# urllib.request

---

> The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.

## urlopen

... öffnet eine URL. (surprise)

    urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

**url** kann ein String sein, wie 'http://python.org' oder 'ftp://store.stuff.de', oder eine komplexere Anfrage in Form eines Request objects sein.  
**data** enthält Daten, die an den Server gesendet werden. Muss vom Typ `bytes` oder ein iterable von `bytes` Objekten sein.  

Bei URLs mit *http*-Requests wird ein [httplib.client.HTTPResponse](#httpresponse-class) Objekt zurück gegeben.  
Bei _**ftp**_, _**file**_ und _**data**_ ein urllib.response.addinfourl Objekt.


## Request Klasse

    Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

## HTTPResponse Klasse
