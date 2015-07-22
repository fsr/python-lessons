---
title: re - Regular Expressions
---

# Syntax

---

Wie auch bei anderen Sprachen, gibt es in Python regular expressions. Dafür gibt es einige Sonderzeichen:  
**.** (Punkt) Matcht alle Zeichen außer `\n`  
**^** Markiert den Anfang des Stings  
**$** Markiert das Ende des Strings (oder das Zeilenende)  
**\*** Der vorangestellte Charakter muss 0 - n Mal vorkommen  
**+** Der vorangestellte Charakter muss 0 - n Mal vorkommen  

---

**?** Der vorangestellte Charakter muss 0 - 1 Mal vorkommen  
**{m}** Der vorangestellte Charakter muss genau m Mal vorkommen  
**{m,n}** Der vorangestellte Charakter muss m - n Mal vorkommen  
**\\** zum escapen von Sonderzeichen  
**[]** matcht eines der in den Klammern stehenden Zeichen  
**|** ist ein ODER entweder der Character davor oder der danach.

---

Des weiteren gibt es noch spezielle Sequenzen, wie z. B.  
**\\d** für Unicode Ziffern, äquivalent für `[0-9]`  
**\\D** ist das Gegenteil, alles was keine Unicode Ziffern sind  
**\\s** für alle Whitespace Charaktere, das entspricht [ \\t\\n\\r\\f\\v]  
**\\S** entspricht wieder dem Gegenteil  
**\\w** für alle Unicode Zeichen [a-zA-Z0-9_]  
**\\W** für alle Nicht-Unicode Zeichen  

# Methoden

---

    compile(pattern, flags=0)
Wandelt einen String in ein regular expression Objekt um  

    search(pattern, string, flags=0)
Sucht in `string` nach dem Pattern `pattern`

    match(pattern, string, flags=0)
Sucht am Begin des Strings nach dem Pattern

    fullmatch(pattern, string, flags=0)
Der komplette String und das Pattern müssen übereinstimmen.

---

    findall(pattern, string, flags=0)
Gibt eine Liste von Strings mit allen passenden Übereinstimmungen zurück  

    finditer(pattern, string, flags=0)
Gibt einen Iterator, welcher `match` Objekte beinhaltet zurück  

Die restlichen Funktionen können in den [Docs](https://docs.python.org/3/library/re.html) gefunden werden.

# regular expression Objekt

---

Ein solches Objekt hat im Großen und Ganzen die selben Methoden, jedoch ohne zusaätzliches Pattern, da das Objekt an sich bereits ein Pattern enthält.

# Match Objekt

---

    start([group])
Gibt die Startposition des Patterns im String zurück  

    start([group])
Gibt die Endposition des Patterns im String zurück  

    span([group])
Gibt ein Tuple zurück `(m.start([group]),m.end([group]))`
