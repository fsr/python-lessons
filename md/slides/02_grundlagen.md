---
title: Grundlagen von Python
---
# Scriptcharakter

---


-   Beim Ausführen oder Importieren wird der Code im obersten Level des
    Moduls (der .py Datei) ausgeführt
-   Funktionen, Klassen und globale Variablen werden üblicherweise
    auf dem obersten Level definiert
-   Imports anderer Python Module werden auch hier ausgeführt

---

Soll das entsprechende Modul ausführbar sein und nicht
nur als Bibliothek dienen, definiert man üblicherweise eine _main_-Funktion.  
Zusätzlich fügt man am Ende des Moduls die _Boilerplate_ ein.

---

```python
def main():
    pass

if __name__ == '__main__':
    main()

```

---

-   Python Code wird nicht kompiliert, sondern beim importieren in
    Python Bytecode übersetzt
-   Bytecode wird auf einer VM ausgeführt
-   Kein Memory Management nötig, alles sind Referenzen
-   Syntaxerror wird beim Importieren geworfen
-   Andere Fehler findet man erst, wenn die betreffende Zeile
    ausgeführt wird.

# Programmier-paradigmen

## Imperatives Programmieren

-   Python ist vor allem eine imperative und objektorientierte Sprache
-   reine Funktionen und Variablen können auf oberster Ebene definiert
    werden
-   Variablen, Klassen und Funktionen sind ab der Ebene sichtbar, in der
    sie eingeführt werden

## Das Scoping Problem

Variablen sind zwar nach innen sichtbar, werden aber beim Reassignment
innerhalb der Funktion neu angelegt und verschwinden so aus dem Scope.

---

```python
var = 12

def foo():
    # erwarteter Effekt: var wird auf 9 gesetzt
    var = 9

def main():
    print(var)  # -> gibt 12 zurueck
    foo()
    print(var)  # -> Erwartung: gibt 9 aus.
                # Realitaet: gibt 12 aus.

if __name__ == '__main__':
    main()
```

---

**Die Lösung:**
```python
var = 12

def foo():
    global var
    # global sagt dem Interpreter, dass er hier auf die
    # oberhalb definierte Variable zurueckgreifen soll
    var = 9

def main():
    print(var)  # -> gibt 12 zurueck
    foo()
    print(var)  # -> gibt jetzt 9 aus

if __name__ == '__main__':
    main()
```

## Objektorientiertes Programmieren

-   Python ist auch fundamental objektorientiert
-   Alles in Python ist ein Objekt
-   Selbst die Datentypen `int`, `bool`, `str` und `type` sind Instanzen
    von `object` und haben folglich Methoden und Attribute
-   Der Typ jedes Wertes und jeder Variablen lässt sich mit `type()`
    ermitteln


# Klassen und Attribute

---

-   Typen in Python werden ausgedrückt durch Klassen (Keyword `class`)
-   Klassen dienen als Vorlage bzw. Schablone -&gt; Objekte sind dann
    Instanzen davon
-   Die Besonderheit: alle Variablen und Werte sind Instanzen von
    `object`  

---

`object` und alle Typen selbst sind widerum Objekte, genauer gesagt
Instanzen vom Typ `type` und `type` widerum ist eine Subklasse von
`object`.

---

-   Klassen und Objekte können selbst auch Variablen tragen (ähnlich wie
    in Java)
-   Man unterscheidet dabei zwischen Klassenattributen und
    Instanzattributen

---

**Klassenattribute**  
werden für die Klasse definiert und sind für alle Instanzen gleich

**Instanzattribute**  
werden außerhalb der Klassendefnition hinzugefügt (normalerweise
im Initialisierer) und sind für jede Instanz unterschiedlich.

---

-   Zugriff auf Attribute über Punktnotation (wie in Ruby/Java)
-   Attribute werden wie Variablen mithilfe von `=` gesetzt
-   Man kann Objekten jederzeit neue Attribute hinzufügen (auch
    `type`-Objekten)
-   Ist außerhalb des Initialisierers nicht empfehlenswert

# Methoden

---


-   Methoden sind Funktionen
-   Allgemeiner Typ von Methoden ist daher `function`
-   Methoden liegen im Namespace der zugehörigen Klasse, müssen daher
    mit `ClassName.method_name()` angesteuert werden (oder auf dem
    Objekt aufgerufen werden)

---

-   Methoden haben ein implizites erstes Argument (typischerweise “self”
    genannt, kann aber variieren)
-   Beim Aufruf auf einer Instanz wird das Objekt selbst automatisch
    übergeben

## Spezielle Methoden

Dies sind Methoden die auf den meisten
Grundlegenden Datenstrukturen implementiert sind, z.B. `object`.\
Die Folgenden beginnen und enden normalerweise mit zwei Unterstrichen.

---

**Initialisierer**  
Oft auch (fälschlicherweise) Konstruktor genannt.  
Name: `__int__`  
Wird immer aufgerufen wenn eine neue Instanz der Klasse erstellt wird.

---

**Finalisierer**  
Oft auch (fälschlicherweise) Destructor genannt.  
Name: `__del__`  
Wird immer aufgerufen wenn das Objekt vom Garbage Collector aufgeräumt wird.  
(selten verwendet)

---

**String Konvertierer**  
Äquivalent zu Java’s `toString` Methode. Name: `__str__`

**String Repräsentation**  
Ähnlich wie `__str__` aber gedacht für eine für Debug verwendbare Repräsentation anstatt für Output wie `__str__`.

## Klassen- und Objektattribute im Detail

---

Klassenattribute sind für jede Instanz eines Objektes gleich.
```python
class TestClass():
    # jeder Instanz wird bei Erstellung bereits
    # dieses Attribut zugewiesen
    num = 12

def main():
    a = TestClass()
    b = TestClass()
    # beide Variablen haben fuer 'num' von der
    # Erstellung an den gleichen Wert

    # das Aendern der Variable ueberschreibt das
    # Klassenattribut mit einem Instanzattribut
    a.num = -3
    print(b.num)  # -> liefert immer noch 12
```

---

Gewöhnlich definiert man Instanzattribute allerdings im
*Initialisierer*.
```python
class Human():
    def __init__(self, firstname, lastname):
        # die beiden Parameterwerte werden in Instanz-
        # attributen gespeichert.
        self.firstname = firstname
        self.lastame = lastname

def main():
    # instanziiert zwei Objekte vom Typ 'Human'
    matthias = Human("Matthias", "Stuhlbein")
    john = Human("John", "Doe")
```
Instanzattribute sollten immer in \_\_init\_\_ definiert werden, um
sicherzustellen, dass alle Instanzen die gleichen Attribute haben
