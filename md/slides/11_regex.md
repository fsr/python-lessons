---
title: re - Regular Expressions
---

# Grundlage

---

Das `re` Modul der python standard library ist die Python Implementierung von regulären Ausdrücken.

Reguläre Ausdrücke werden verwendet um die Struktur von Text/Sprachen zu beschreiben.

---

Ein erstellter regulärer Ausdruck kann verwendet werden um:

- die Struktur eines Textes zu überprüfen
- bestimmte Teile eines Textes zu extrahieren

---

Die Anwendung eines regulären Ausdruckes nennt man Matching.

Matcht der reguläre Ausdruck einem String, bedeutet dies, dass der String die Struktur hat die der reguläre Ausdruck beschreibt.

Reguläre ausdrücke werden oft auch "regex" genannt (kurz für regular Expression).

# Matching Regeln

---

Jeder Buchstabe und jede Zahl matcht immer **einmal** sich selbst.

d.h.

Der String `"a"` matcht der regex `"a"`.  
Der String `"abc"` matcht der regex `"abc"`, nicht aber regex `"a"`.  
`"4"` matcht `"4"`, nicht aber `"5"`, `"a"` oder `"41"` usw.


## Sonderzeichen

`.` (Punkt) matcht **einem** beliebingen Schriftzeichen, außer `\n` (newline)

Für die regex `"."` gilt

- `"a"` matcht
- `"b"` matcht
- `"4"` matcht
- `"ab"` matcht nicht, denn `"."` ist nur ein Zeichen und `"ab"` sind zwei.

---

`[]` matcht jedem der in den Klammern stehenden Zeichen, jedoch nur **einmal** (wie bei `.`).

Für die regex `"[abg]"` gilt also

- `"a"` matcht
- `"b"` matcht
- `"g"` matcht
- `"ab"` matcht nicht (zwei zeichen matchen nicht einem)

---

`\` zum escaped ein Sonderzeichen.

Alle hier aufgeführten Sonderzeichen können nicht in einem Pattern vorkommen, als das, was sie eigentlich bedeuten, dafür müssen sie extra markiert werden.

- `"\\"` als Pattern matcht auf den String `"\"`
- `"\."` als Pattern matcht auf den String `"."`

---

`^` Matcht dem Anfang eines Stings  
Es matcht alles, was bis zum ersten auftreten des Patterns existert

Für die regex `"^a"` ergibt sich also

- `"a"` matcht
- `"ba"` matcht
- `"aba"` matcht nicht, da nach "a" noch weitere Zeichen folgen

---

`$` Matcht dem Ende eines Strings (oder das Zeilenende)  

Für die regex `"a$"` folgt daraus

- `"a"` matcht
- `"ab"` matcht
- `"ba"` matcht nicht, da der Anfang nciht stimmt
- `"aba"` matcht

---

`|` ist ein ODER entweder der Character davor oder der danach.

Für die regex `"a|b"` gilt

- `"a"` matcht
- `"b"` matcht
- `"ab"` matcht nicht, da `"a|b"` mit [ab] gleichzusetzen ist

---

Regexes bauen sich dann aus kleineren regexes auf.  
So kann man auch sagen, wie häufig ein Zeichen auftreten soll.

---

`*` Die vorangestellte Charakter muss 0 - n Mal vorkommen

Für die regex `"a*"` gilt

- `""` matcht
- `"a"` matcht
- `"aa"` matcht
- `"aaaab"` matcht nicht, da ein anderes Zeichen als "a" vorkommt

---

`+` Der vorangestellte Charakter muss 1 - n Mal vorkommen  

Für die regex `"a+"` gilt

- `""` matcht nicht, da es kein mal vorkommt
- `"a"` matcht
- `"aa"` matcht
- `"ab"` matcht nicht, da ein anderes Zeichen als "a" vorkommt

---

`?` Der vorangestellte Charakter muss 0 - 1 Mal vorkommen  

Für die regex `"a?"` gilt

- `""` matcht
- `"a"` matcht
- `"aa"` matcht nicht, da das Zeichen öfter, als nur ein mal vorkommt

---

`{m}` Der vorangestellte Charakter muss genau m Mal vorkommen

Für die regex `"y{3}"` gilt

- `yyy` matcht
- `"y"` matcht nicht, da es zu wenige Zeichen sind
- `"yyyy"` matcht nicht, da es mehr Zeichen sind

---

`{m,n}` Der vorangestellte Charakter muss m - n Mal vorkommen

Für die regex `"y{2,5}"` gilt

- `yyy` matcht
- `"y"` matcht nicht, da es zu wenige Zeichen sind
- `"yyyy"` matcht
- `"yyyyyy"` matcht nicht, da es zu viele Zeichen sind

---

Des weiteren gibt es noch spezielle Sequenzen, wie z. B.  
`\d` für Unicode Ziffern, äquivalent für `[0-9]`  
`\D` ist das Gegenteil, alles was keine Unicode Ziffern sind  
`\s` für alle Whitespace Charaktere, das entspricht `[ \\t\\n\\r\\f\\v]`  
`\S` entspricht wieder dem Gegenteil  
`\w` für alle Unicode Zeichen [a-zA-Z0-9_]  
`\W` für alle Nicht-Unicode Zeichen  

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
