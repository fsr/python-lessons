# Grundlagen: Mails senden


## Das Modul `smtplib`


Das Modul `smtplib` definiert eine SMTP**\***-Client Session, die genutzt werden kann, um
von jedem beliebigen, internetfähigen Gerät E-Mails zu verschicken.  

**\****SMTP* steht für Simple Mail Transfer Protocol und ist das Standard-Protokoll zum E-Mail Versand.

---

### Verbindung zum Server


Die smtplib kann sich zu
einem SMTP-Server verbinden

```python
smtplib.SMTP(host=’ ’, port=0, local_hostname=None,
            [timeout,] source_address=None)
```

Der Server kann zum einen als einheitlicher `String` (inkl. Port) oder
einzeln als `host` und `port` angeben werden.

---

### Login auf dem Server


Heutzutage Zeit arbeiten die meisten SMTP-Server mit `TLS`, um eine sichere Verbindung zu gewährleisten. Diese muss mithilfe von der Methode `starttls()` hergestellt werden.  
Der eigentliche Login erfolgt im Anschluss durch:    

```python
SMTP.login(user, password, ∗, initial_response_ok=True)
```

Der Parameter `initial_response_ok` kann in unserem Fall vernachlässigt
werden.

---

### Senden der Mail


Das tatsächliche Versenden der Mail funktioniert dann mit folgender Methode:  

```python
SMTP.sendmail(from_addr, to_addrs, msg, mail_options=[],
              rcpt_options=[])
```

Jedoch lässt sich das ganze auch mit einem `MIME`-Objekt vereinfachen, auf das später noch eingegangen wird.  
Dieses wird mit `send_message()` versendet.

---

### Schließen der Verbindung

Zum Schluss darf nicht vergessen werden, die Verbindung zum SMTP-Server wieder zu schließen.  
Dies geschieht mit der Methode `quit()` oder man stellt die Verbindung
mithilfe eines `Filehandlers` her.


#Komplexere Mails senden


## Das Modul `email`


Um mehr Möglichkeiten zur Gestaltung der E-Mail zu haben, lohnt sich die Verwendung des Moduls
`email`.
Mit `email.mime` lassen sich Emails individuell bauen und
zusammensetzen. Außerdem kann man mehrteilige Mails und Mails mit
Anhängen (z.B. Bildern) erstellen.

---

### Die Klasse `MIMEText`

Die Klasse `email.mime.text.MIMEText()` erstellt ein MIME Objekt, welches
hautpsächlich aus Text besteht und einfach dem SMTP-Objekt übergeben
werden kann:  
```python
email.mime.text.MIMEText(_text, _subtype='plain', _charset=None)
```

---

\_text: Ein String, der den Inhalt der Nachricht enthält.

\_subtype: Der Untertyp des Objekts, per default `plain`

charset: Der Zeichensatz, der zur Kodierung der Zeichen verwendet
    werden soll. Standardmäßig `us-ascii` oder `utf8`, abhängig von dem
    eingegebenen Text.

---

### Die Meta-Felder


Wenn das `MIMEText` Objekt instanziiert ist, muss dieses mit weiteren Informationen ergänzt werden:  

```python
# set the sender of your mail
message['From'] = 'Sender name <sender@example.com>'
# set the receiver of your mail
message['To'] = 'Receiver name <receiver@example.com>'

message['Subject'] = 'Betreff der E-Mail'
```

Die Message lässt sich außerdem noch um einen `Cc` oder einen `Bcc`
erweitern.
