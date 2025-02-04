from Mediamarkt import *
from Standardkunde import *
from Exklusivkunde import *

# Märkte erzuegen
mm1 = Mediamarkt("Mediamarkt Lengfeld")
mm2 = Mediamarkt("Mediamarkt Stadt")


# Kunden erzeugen
stefan = Exklusivkunde("Stefan")
nils = Standardkunde("Nils")
katharina = Standardkunde("Katharina")

# Kunden registrieren sich bei Medimarkt Stadt
mm1.addObserver(stefan)
mm1.addObserver(nils)
mm1.addObserver(katharina)

# Kunden registrieren sich bei Medimarkt Lengfeld
mm2.addObserver(stefan)
mm2.addObserver(nils)



# Angebote kommen
mm1.setAngebot("PS6")
mm2.setAngebot("PS6")
