
##############################################################################
from lehrling import lehrling
from meister import meister
###########################################################################

# create object and build object reference
eder = meister()
henning = lehrling(eder)


# Optional Fragment - IF
# Henning fragt den Meister, ob sie Eis essen wollen

if(henning.getFleissig() == True):
    henning.frageNachPause()

henning.fegen()



# Loop und if/else
# # Henning bekommt den Auftrag vom Meister, dass er 3 Stühle baut
henning.baueStuehle(3)

for i in range (3):
    eder.pruefeArbeit(i)
    
    


 




