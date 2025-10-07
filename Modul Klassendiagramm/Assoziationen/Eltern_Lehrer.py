class Eltern:
    def __init__(self, name):
        self.__name = name
        self.__interesse = True

    def getElternname(self):
        return self.__name

    def anrufen(self):
        print(f"{self.__name} wird angerufen.")


class Lehrer:
    def __init__(self, name):
        self.__name = name
        self.__interesse = True

    def getLehrername(self):
        return self.__name

    def anrufen(self):
        print(f"{self.__name} wird angerufen.")

# Beispielhafte Nutzung
lehrer1 = Lehrer("Herr Weber")
eltern1 = Eltern("Frau Schulz")


