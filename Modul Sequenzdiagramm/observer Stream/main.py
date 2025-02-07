from FilmDaten import FilmDaten
from AnzeigeNeu import AnzeigeNeu
from AnzeigeBeliebt import AnzeigeBeliebt

if __name__ == "__main__":
    
    # Erstelle ein Subjekt und ein paar Beobachter
    
    filmtest = FilmDaten()
    neu = AnzeigeNeu(filmtest)
    beliebt = AnzeigeBeliebt(filmtest)
    

    
    # Aktualisiere Filmdaten und benachrichtige Beobachter
    filmtest.set_data("Terminator","12 Geschworenen","Star Wars")
    filmtest.set_data("Oppenheimer","The Creator","Dolly Darko")