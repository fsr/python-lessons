---
---

class Alert
  close: (child) -> child.parentNode.remove()

  constructor: ->
    for alert in document.getElementsByClassName('alert')
      for closer in alert.getElementsByClassName('close')
        closer.addEventListener("click", -> alert.remove())

window.onload = ->
  window.alert = new Alert()
