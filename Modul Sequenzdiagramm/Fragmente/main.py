
##############################################################################
from lehrling import lehrling
from meister import meister
###########################################################################

# create object and build object reference
eder = meister()
henning = lehrling(eder)


# No. 1
if(henning.getFleissig() == True):
    print(henning.frageNachPause())

henning.fegen()


# No. 2
henning.baueStuehle(3)
    

# No.3 
for i in range (3):
    eder.pruefeArbeit(i)



 




