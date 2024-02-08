from FilmDaten import FilmDaten
from AnzeigeNeu import AnzeigeNeu




if __name__ == "__main__":
    
    # Erstelle ein Subjekt und ein paar Beobachter
    
    filmtest = FilmDaten()
    zeige = AnzeigeNeu(filmtest)

    
    # Füge Beobachter hinzu
    filmtest.addChangeListener(zeige)
    
    
    # Aktualisiere Filmdaten und benachrichtige Beobachter
    filmtest.set_data("Terminator","12 Geschworenen","Star Wars")
    filmtest.set_data("John Wick","Sherlock Holmes - Spiel im Schatten","Jenseits von Afrika")