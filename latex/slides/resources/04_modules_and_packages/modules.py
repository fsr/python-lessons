# Importieren des kompletten Moduls incdec
import incdec

# Die Funktionen koennen wie folgt aufgerufen werden:
incdec.inrement(3)
# => 4
incdec.decrement(3)
# => 2

# Importieren einzelner Funktionen
from incdec import increment

# Diese kann jetzt sofort aufgerufen werden
increment(3)
# => 4

# Alias fuer Module verwenden
import incdec as plusoneminusone

plusoneminusone.inrement(3)
# => 4
