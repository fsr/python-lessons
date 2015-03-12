# Über diesen Kurs
- 12 Kurseinheiten
- setzt grundlegende Programmierkentnisse voraus
- Ressourcen
    - [auditorium](http://auditorium.inf.tu-dresden.de) # TODO add link to our group once it exists
    - Google (python/python 3 meine frage hier) landet oft in der python 2.7 doku (versionsswitcher im menü)
    - [offizielle Dokumentation](docs.python.org)
    - unsere [Github-Organisation](http://github.com/tud-python-courses)
- Hinweis: SCM's sind hilfreich ([git](https://git-scm.com), [mercurial](http://mercurial.selenic.com/))


# Python Interpreter
- Die zwei verbreitet verwendeten Python Versionen sind 2.7 und 3.4, wir werden 3.4 nutzen, weil es cooler ist und bessere Features hat
- Python kann auf [hier](http://www.python.org) heruntergeladen und installiert werden oder mit dem Paketmanager eurer Wahl. (Das Paket sollte `python3` und `python3-dev` sein, außer unter Arch)
- Python funktioniert besser unter Linux und Mac (ist aber okay unter Windows)
- Den Interpreter startet man mit `python3` im Terminal oder mit `Python.exe`
- Der Interpreter stellt die volle Funktionoalität von Python bereit, einschließlich dem Erstellen von Klassen und Funktionen


# Python Scripte
- __Editor__ empfohlen (das ist was wir im Kurs benutzen)
    - [atom](https://atom.io) (weil github)
    - [Sublime Text 3](http://www.sublimetext.com/3) (winrar-free)
    - [Notepad++](http://notepad-plus-plus.org) (free)
    - [cloud9](https://c9.io) (online, free für open source projekte)
    - vim/emacs (free)
- __IDE's__  
Benutzen wir hier nicht, da wir kein Kurs über eine IDE machen, sondern über Python selbst (wir beantworten im Kurs keine Fragen zu IDE Problemen)
    - [PyCharm](https://jetbrains.com/pycharm) (free + professional für Studenten)
    - [Wing](https://wingware.com/) (kostenpflichtig)
- __Struktur__
    - Python Scripte sind Textdateien, die auf `.py` enden
    - Python Packages sind ordner mit einer `__init__.py` Datei (behandeln wir später)


# Grundlagen der Sprache
Python ist eine schwach typisierte Scriptsprache (weakly typed scripting language). Es gibt Typen (anders als in JavaSript), aber Variablen haben kene festen Typen.

- __Kommentare__:

```py
# in python nur einzeiler Kommentare

def my_function(params):
    """
    Oder docstrings wie dieser,
    aber nur zu beginn einer Funktions- oder Klassendefinition
    """
    pass
```

- __builtin Datentypen__:

| Name | Funktion |
|:----:|:---------|
| `object` | Basistyp, alles erbt von `object` |
| `int` | Ganzzahl "beliebiger" Größe |
| `float` | Kommazahl "beliebiger" Größe |
| `bool` | Wahrheitswert (`True`, `False`) |
| `None` | Typ des `None` objektes |
| `type` | Grundtyp aller Typen (z.B. `int` ist eine Instanz von `type`) |
| `list` | standard Liste |
| `tuple` | unveränderbares n-Tupel |
| `set` | (mathematische) Menge von Objekten |
| `frozenset` | unveränderbare (mathematische) Menge von Objekten |
| `dict` | Hash-Map |

# Das erste Programm
Ein simples "Hallo Welt"-Programm

```py
def my_function():
    print('Hallo Welt!')

if __name__ == '__main__':
    my_function()
```

## Wichtige Eigenschaften
- Keine Semikolons
- Kein geschweiften Klammern für Codeblöcke
- Einrückungen zeigen Codeblöcke an
- Funktionsaufrufe immer mit runden Klammern
- Funktionen definieren mit `def <funktionsname>([parameter_liste, ...]):`
- Variablen mit der Struktur `__name__` sind spezielle werte (gewöhnlich aus `builtin` oder methoden von standardtypen)  
  z.B. `__file__` ist immer der Name des scriptes (in welchem `__file__` aufgerufen wird),  
  `__builtin__` ist das module mit den immer verfügbaren funktionen und datentypen wie `list` oder `tuple`

# Operatoren
- __mathematisch:__ `+`, `-`, `*`, `/` 
- __boolean:__  
  `<`, `>`, `<=`, `>=`, `==` (Wert gleich), `is` (gleiches Objekt/gleiche Referenz)
- __logisch:__ `and`, `or`, `not`  
  `(a && b) || (!c)` aus C oder Java entspricht `(a and b) or not c` in Python
- __bitweise:__ `&`, `|`, `<<`, `>>`, `^` (xor), `~` (invertieren)
- __Accessoren:__ `.` (für Methoded und attribute), `[]` (für Datenstrukturen mit Index)

# Namenskonventionen
- __Klassen:__ *PascalCase*, alles direkt zusammen, groß beginnend und jedes neue Wort groß
- __Variablen, Funktionen, Methoden:__ *snake_case*, alles klein und Wörter mit Unterstrich getrennt  
  __Merke:__ Da '-' ein Operator ist, ist es in Namen von Variablen, Funktionene etc. __*nicht*__ zulässig (damit Python eine Kontextfreie Sprache ist)
- __protected Variablen, Funktionen, Methoden:__ beginnen mit einem Unterstrich `_` oder mit zweien `__` für private  
  __Merke:__ Python hat kein Zugriffsmanagement. Die Regel mit dem Unterstrich ist nur eine Konvention um zu verhindern, dass ander Teile des Codes nutzen, der eine hohe Wahrscheinlichkeit hat in Zukuft verändert zu werden.

# Strings
## Grundlagen
- Der Typ eines Strings ist `str`.
- Strings sind in Python immutable (nicht veränderbar). Jede String Operation erzeugt einen neuen String.
- Ein String kann erzeugt werden mit einer Zeichenkette in Anführungszeichen, `''` oder `""` (beide sind äquivalent).
- rohe Strings mir dem Präfix `r`, `r"mystring"` oder `r'mystring'`
- Strings in Python 3 sind UTF-8 encoded.

## Verknüpfen
- Strings können durch Konkatenation verknüpft werden  
  ```py
  'Hallo' + '_' + 'Welt' #  => 'Hallo_Welt'
```
- Listen, Tupel etc. von Strings können via `str.join` verknüpft werden
  ```py
'_'.join(['Hallo', 'Welt']) #  => 'Hallo_Welt'
    ```
    Dabei ist der String auf welchem die Methode aufgerufen wird der Separator.

## Formatierung


Wir wollen den String `'my string 4 vier'` erzeugen.

```py
# mit `str.format()`  

'my string {} {}'.format(4, 'vier')
# in Reihenfolge der argumente

'my string {number} {name}'.format(name='vier', number=4)`
# via Name, Reihenfolge egal

'my string {number} {}'.format('vier', number=4)
# oder beides kombiniert


# und mit dem %-Operator

'string %d %s' % (4, 'vier')
# in Reihenfolge

'string %(number)d %(name)s' % {number:4, name:'vier'}
# via Name
  ```
