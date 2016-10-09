# Das Package urllib

---

Das Package `urllib` ist eine nützliche Sammlung mehrerer Module zur Arbeit mit URLs.

## urllib.request

Das Modul `urllib.request` enthält Funktionen und Klassen, welche beim Öffnen
von URLs (vor allem über HTTP) helfen.

---

Unterstützt werden:

-   verschiedene Authentifizierungsarten
-   Weiterleitungen
-   Cookies
-   und mehr...

---

### Öffnen einer URL

Das Öffnen einer URL wird über die Funktion `urlopen()` realisiert:

```python
import urllib.request

urllib.request.urlopen(url, data=None, [timeout, ] *,
                       cafile=None, capath=None, cadefault=False,
                       context=None)
```

---

**url**

ein String für simple URLs oder ein `Request` Objekt für komplexere
Anfragen

**data**

Daten, die an den Server gesendet werden sollen.  
Vom Typ `bytes` oder ein Iterable von `bytes` Objekten.

---

**Rückgabewerte**

Bei URLs mit http-Requests:  
`httplib.client.HTTPResponse` Objekt

bei ftp, file und data:  
`urllib.addinfourl` Objekt



## Request Klasse

---

Um komplexere Anfragen stellen zu können, kann man Request Objekte verwenden:

```python
urllib.request.Request(url, data=None, headers={},
                       origin_req_host=None, unverifiable=False,
                       method=None)
```

---

**url**

muss String mit gültiger URl sein

**data**

wie bei *urlopen*

---

**headers**

`dict` mit `{Header-Name : Header-Value, ...}` oder  
`list` von Tupeln mit `[(Header-Name, Header-Value), ...]`

**method**

String, der Art des HTTP Request angibt (`HEAD`, `GET`, `POST`, ...)

---

### Beispiel

```python
import urllib

r = urllib.request.Request(
    'http://python.org',
    headers={'content-type': 'application/json'},
    method='PUT'
)
```

---

Die Request Klasse kann man Verwenden zum:

-   Kontrollieren der gesendeten Header *(z.B. Content-Type
    oder User-Agent)*
-   Kontrollieren der Method `POST`, `PUT` oder `HEAD`



## HTTPResponse Klasse

---

```python
http.client.HTTPResponse(sock, debuglevel=0,
                         method=None, url=None)
```

---

Objekte dieser Klasse werden nicht direkt vom User erstellt.  
Klasse enthält Funktionen und Variablen wie:

-   `read()` - gibt zurückgelieferten Inhalt zurück
-   `getheader()` oder `getheaders()` liefert einen/alle Header zurück
-   `status` gibt den HTTP Statuscode zurück
-   `version` gibt die HTTP Version zurück


# Andere Module

---

Das Package `urllib` enthält außerdem folgende Module:

---

`urllib.error`  
Enthält Exceptions, die von `urllib.request` geworfen werden.

---

`urllib.parse`  
Zum Parsen von URLs.

---

`urllib.robotparse`  
Zum Parsen der *robots.txt* von Webseiten.


# Das Requests-Modul

## Installation

Das Requests Modul ist eine gute und für Menschen verständliche Alternative zu
`urllib.requests`, das HTTP Requests vereinfacht.

---

Das Requests Package lässt sich ganz einfach über **pip** installieren:  
`pip install requests`

---

### Beispiel

```python
r = requests.get('https://api.github.com/user',
                 auth=('user', 'pass'))

r.status_code   # -> 200
r.headers['content-type']
# -> 'application/json; charset=utf8'
r.encoding      # -> 'utf-8'
r.text          # -> u'{"type":"User"...'
r.json()
# -> {u'private_gists': 419, u'total_private_repos': 77, ...}
```
---

Ruft die API-Seite von **GitHub** auf und authentifiziert sich mit
Nutzername und Passwort.
