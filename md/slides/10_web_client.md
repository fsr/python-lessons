---
title: Python als Webclient
---

# urllib.request

---

> The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.


## urlopen

... öffnet eine URL. (surprise)

    urlopen(url, data=None, [timeout, ]\*, cafile=None, capath=None, cadefault=False, context=None)

**url** kann ein String sein, wie 'http://python.org' oder 'ftp://store.stuff.de', oder eine komplexere Anfrage in Form eines Request objects sein.  
**data** enthält Daten, die an den Server gesendet werden. Muss vom Typ `bytes` oder ein iterable von `bytes` Objekten sein.  

Bei URLs mit *http*-Requests wird ein httplib.client.HTTPResponse Objekt zurück gegeben.  
Bei *ftp*, *file* und *data* ein urllib.response.addinfourl Objekt.


## Request Klasse

    Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

**url** muss ein String mit einer gültigen URL sein  
**data** wie bei urlopen
**headers** entweder ein `dict` mit { Header-Name : Header-Value, ... } oder eine `list` von Tupeln mit [( Header-Name, Header-Value ), ...]  
**method** ein String, welcher die Art des HTTP Request angibt (`HEAD`, `GET`, `POST`,...)

---

Die Request Klasse wird verwendet, wenn man z.B. die gesendeten Header, wie 'Content-Type' oder 'User-Agent' oder die Method, wie 'POST', 'PUT' oder 'HEAD' kontrollieren möchte.

```python
r = Request(
    'http://python.org',
    headers={ 'content-type': 'application/json' },
    method='PUT'
)
```

## HTTPResponse Klasse

Die Instanzen der HTTPResponse Klasse werden nicht vom Nutzer erstellt.

    http.client.HTTPResponse(sock, debuglevel=0, method=None, url=None)

Sie beinhalten Funktionen wie `read()`, `getheader()` oder `getheaders()` und Variablen wie `status` oder `version`.

`read()` gibt zurückgelieferten Ihnalt aus,
`getheader()` und `getheaders()` einen oder alle Header

`status` gibt den HTML Statuscode an
`version` die HTML version

# Requests

---

Das [Requests](https://github.com/kennethreitz/requests) Modul ist eine gute Alternative zu `urllib.request`.  Es vereinfacht HTTP Requests.

```python
>>> r = requests.get('https://api.github.com', auth=('user', 'pass'))
>>> r.status_code
204
>>> r.headers['content-type']
'application/json'
```
