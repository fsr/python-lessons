# Über diesen Kurs

---

-   12 Kurseinheiten
-   setzt grundlegende Programmierkenntnisse voraus
-   Ressourcen
    -   [auditorium](http://auditorium.inf.tu-dresden.de)
    -   Google (python/python3 meine frage hier) landet oft in der
        python 2.7 Doku (Versionsswitcher im Menü)
    -   [offizielle Dokumentation](docs.python.org)
    -   unsere [Github-Organisation](https://github.com/fsr)
    -   Hinweis: SCM’s sind hilfreich ([git](https://git-scm.com),
    [mercurial](http://mercurial.selenic.com/))


<div class="notes">
Es ist für 11 Kurseinheiten offiziell Material vorhanden.
Alle weiteres Stunden sollten sich auf Wünsche der Studenten beziehen.
</div>


# Der Python Interpreter

---

-   Die zwei verbreitet verwendeten Python Versionen sind 2.7 und 3.5,
    wir werden 3.5 nutzen, weil es cooler ist und bessere Features hat
-   Python kann [hier](https://www.python.org/downloads/) heruntergeladen und installiert werden oder mit dem
    Paketmanager eurer Wahl. (Das Paket sollte `python3` und
    `python3-dev` sein, außer unter Arch)

---

-   Python funktioniert am besten unter UNIX (ist aber okay
    unter Windows)
-   Den Interpreter startet man mit `python3` im Terminal oder mit
    `Python.exe`
-   Der Interpreter stellt die volle Funktionalität von Python bereit,
    einschließlich dem Erstellen von Klassen und Funktionen


# Python Scripte

## Editor

empfohlen (benutzen wir im Kurs)

-   [atom](https://atom.io) (weil Github)
-   [Sublime Text 3](http://www.sublimetext.com/3) (“Winrar-free”)
-   [cloud9](https://c9.i) (online, free für open source Projekte)

## IDEs

hilfreich bei größeren Projekten, hier nicht genutzt

-   [PyCharm](https://jetbrains.com/pycharm) (free + professional für Studenten)

## Struktur

-   Python Scripte sind Textdateien, die auf `.py` enden
-   Python Packages sind Ordner mit einer `__init__.py` Datei (behandeln wir später)


# Grundlagen der Sprache

---

Python ist eine schwach typisierte Scriptsprache (weakly typed scripting language). Es gibt
Typen (anders als in JavaScript), aber Variablen haben keine festen
Typen.

---

## Kommentare:
```python
# in python nur einzeilige Kommentare

def my_function(params):
    """
    Oder docstrings wie dieser,
    aber nur zu beginn einer Funktions-
    oder Klassendefinition
    """
    pass
```

---

## builtin Datentypen:

| Name | Funktion |
| :------------- | :------------- |
| `object`   |Basistyp, alles erbt von `object`|
| `int`      |Ganzzahl “beliebiger” Größe|
| `float`    |Kommazahl “beliebiger” Größe|
| `bool`     | Wahrheitswert (`True`, `False`)|
| `None`     | Typ des `None`-Objektes|
| `type`     | Grundtyp aller Typen (z.B. `int` ist eine Instanz von `int`)|

---

| Name | Funktion |
| :------------- | :------------- |
| `list`     | standard Liste|
| `tuple`    | unveränderbares n-Tupel|
| `set`      |(mathematische) Menge von Objekten|
| `frozenset`|  unveränderbare (mathematische) Menge von Objekten|
| `dict`     |Hash-Map|

# Das erste Programm

---

Ein simples “Hallo
Welt”-Programm:
```python
def my_function():
    print('Hallo Welt!')

if __name__ == '__main__':
    my_function()
```

---

## Wichtige Eigenschaften:

-   Keine Semikolons
-   Keine geschweiften Klammern für Codeblöcke
-   Einrückungen zeigen Codeblöcke an
-   Funktionsaufrufe immer mit runden Klammern

---

-   Funktionen definieren mit
```python
def <funktionsname>([parameter_liste, ...]):
```
-   Variablen mit der Struktur `__name__` sind spezielle Werte (gewöhnlich aus `builtin` oder Methoden von Standardtypen)

# Operatoren

---

## mathematisch

`+`, `-`, `*`, `/`

## vergleichend

`<`, `>`, `<=`, `>=`, `==` (Wert gleich), `is` (gleiches Objekt/gleiche Referenz)

---

## logisch

`and`, `or`, `not`  
`￼￼￼(a && b) || (!c)` aus C oder Java entspricht in Python  
`(a and b) or not c`

## bitweise

`&`, `|`, `<<`, `>>`, `^` (xor), `~` (invertieren)

## Accessoren

`.` (für Methoden und Attribute), `[]` (für Datenstrukturen mit Index)

# Namenskonvention

---


## Klassen

*PascalCase*, alles direkt zusammen, groß beginnend und jedes neue Wort groß

## Variablen, Funktionen, Methoden

*snake\_case*, alles klein und Wörter mit Unterstrich getrennt  
**Merke:** Da `-` ein Operator ist, ist es in Namen von Variablen,
Funktionen etc. **nicht** zulässig (damit Python eine Kontextfreie Sprache ist)

---

## protected Variablen, Funktionen, Methoden

beginnen mit einem Unterstrich `_` oder mit zweien `__` für private

---

**Merke**  
Python hat kein Zugriffsmanagement. Die Regel mit dem Unterstrich
ist nur eine Konvention um zu verhindern, dass andere Teile des
Codes nutzen, der eine hohe Wahrscheinlichkeit hat in Zukunft
verändert zu werden.

# Strings

---

## Grundlagen


-   Der Typ eines Strings ist `str`.

-   Strings sind in Python immutable (nicht veränderbar). Jede String
    Operation erzeugt einen neuen String.

-   Ein String kann erzeugt werden mit einer Zeichenkette in
    Anführungszeichen, `''` oder `""` (beide sind äquivalent).

-   rohe Strings mir dem Präfix `r`, `r"mystring"` oder `r'mystring'`

-   Strings in Python3 sind UTF-8 encoded.

---

### Verknüpfen

-   Strings können durch Konkatenation verknüpft werden
```python
’Hallo’ + ’_’ + ’Welt’ # => ’Hallo_Welt’
```
-   Listen, Tupel etc. von Strings können via `str.join` verknüpft
    werden
```python
’_’.join([’Hallo’, ’Welt’]) # => ’Hallo_Welt’
```
     Dabei ist der String, auf welchem die Methode aufgerufen wird,
    der Separator.

---

## Formatierung

Wir wollen den String `'my string 4 vier'` erzeugen.
```python
# mit str.format()

'my string {} {}'.format(4, 'vier')
# in Reihenfolge der argumente

'my string {number} {name}'.format(name='vier', number=4)‘
# via Name, Reihenfolge egal

'my string {number} {}'.format('vier', number=4)
# oder beides kombiniert
```
---

Wir wollen den String `'my string 4 vier'` erzeugen.
```python
￼# und mit dem %−Operator

'string%d%s'%(4, 'vier')
# in Reihenfolge

'string %(number)d%(name)s' % {number:4, name:'vier'}
# via Name
```
