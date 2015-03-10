# Präambel
- 12 Kurseinheiten
- setzt grundlegende Programmierkentnisse voraus
- Ressourcen
    - [auditorium](http://auditorium.inf.tu-dresden.de) <- add link to our group once it exists
    - Google (python/python 3 meine frage hier) landet oft in der python 2.7 doku (versionsswitcher im menü)
    - [offizielle Dokumentation](docs.python.org)
    - unsere [Github-Organisation](http://github.com/tud-python-courses)
- Hinweis: SCM's sind hilfreich ([git](https://git-scm.com))

# Python Interpreter
- kurz Python Versionen (wir nutzen >3.4)
- [python](http://www.python.org) installieren
- Unterschiede von `python` und `python3`
- 1 + 1 / "hello world" (string und int operationen), `print` Befehl


# Python Scripte
- __Editor__ empfohlen (das ist was wir im Kurs benutzen)
    - [atom](https://atom.io) (weil github)
    - [Sublime Text 3](http://www.sublimetext.com/3) (winrar-free)
    - [Notepad++](http://notepad-plus-plus.org) (free)
    - vim/emacs (free)
- __IDE's__  
Benutzen wir hier nicht, da wir kein Kurs über eine IDE machen, sondern über Python selbst (wir beantworten im Kurs keine Fragen zu IDE Problemen)
    - [PyCharm](https://jetbrains.com/pycharm) (free + professional für Studenten)
    - [Wing](https://wingware.com/) (kostenpflichtig)
- __Struktur__
    - Python Scripte sind Textdateien, die auf `.py` enden
    - Python Module sind ordner mit einer `__init__.py` Datei (behandeln wir später)

# Grundlagen der Sprache
Python ist eine schwach typisierte Scriptsprache (weakly typed scripting language). Es gibt Typen (anders als in JavaSript), aber Variablen haben kene festen Typen.

- __Kommentare__: `#  Dies ist ein Kommentar`

- __Grundlegende Datentypen__:

| Name | Funktion |
|------|----------|
| `object` | Basistyp, alles erbt von `object` |
| `int` | Ganzzahl "beliebiger" Größe |
| `float` | Kommazahl "beliebiger" Größe |
| `bool` | Wahrheitswert (True, False) |
| `None` | Typ des `None` objektes |
| `type` | Grundtyp aller Typen (z.B. `int` ist eine Instanz von `type`) |
| `list` | standard Liste |
| `tuple` | unveränderbares n-Tupel |
| `set` | Menge von Objekten |
| `frozenset` | unveränderbare Menge |
| `dict` | Hash-Map |
