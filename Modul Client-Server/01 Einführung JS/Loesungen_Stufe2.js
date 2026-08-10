// Daten
let buecher = [
    {
        id: 1,
        titel: "JavaScript für Einsteiger",
        autor: "Müller",
        seiten: 300,
        ausgeliehen: false
    },
    {
        id: 2,
        titel: "Python Grundlagen",
        autor: "Schmidt",
        seiten: 450,
        ausgeliehen: true
    },
    {
        id: 3,
        titel: "SQL leicht gemacht",
        autor: "Weber",
        seiten: 280,
        ausgeliehen: false
    },
    {
        id: 4,
        titel: "Algorithmen und Datenstrukturen",
        autor: "Koch",
        seiten: 520,
        ausgeliehen: true
    },
    {
        id: 5,
        titel: "Webentwicklung mit HTML und CSS",
        autor: "Fischer",
        seiten: 350,
        ausgeliehen: false
    },
    {
        id: 6,
        titel: "Programmieren mit C#",
        autor: "Meier",
        seiten: 420,
        ausgeliehen: false
    },
    {
        id: 7,
        titel: "Netzwerktechnik kompakt",
        autor: "Braun",
        seiten: 240,
        ausgeliehen: true
    },
    {
        id: 8,
        titel: "Linux Administration",
        autor: "Müller",
        seiten: 390,
        ausgeliehen: false
    },
    {
        id: 9,
        titel: "Objektorientierte Programmierung",
        autor: "Schmidt",
        seiten: 480,
        ausgeliehen: true
    },
    {
        id: 10,
        titel: "IT-Sicherheit in der Praxis",
        autor: "Becker",
        seiten: 330,
        ausgeliehen: false
    }
];

// Aufgabe 2.1 searchTitel
function findBookByTitel(titel){
 for(let buch of buecher){
  if(buch.titel===titel) return buch;
 }
 return null;
}

console.log(findBookByTitel("Programmieren mit C#"))

// Aufgabe 2.2 Bücher eines Autos anzeigen
function getMostPopularAuthor() {

    let statistik = {};

    for (let buch of buecher) {

        if (statistik[buch.autor]) {
            statistik[buch.autor]++;
        } else {
            statistik[buch.autor] = 1;
        }

    }

    let besterAutor = "";
    let maxAnzahl = 0;

    for (let autor in statistik) {

        if (statistik[autor] > maxAnzahl) {
            maxAnzahl = statistik[autor];
            besterAutor = autor;
        }

    }

    return {
        autor: besterAutor,
        anzahl: maxAnzahl
    };
}

console.log(getMostPopularAuthor())
// 2.3 Ausleihquote berechnen

function getBorrowRateByAuthor() {

    let statistik = {};

    // Anzahl der Bücher und ausgeliehenen Bücher pro Autor zählen
    for (let buch of buecher) {

        if (!statistik[buch.autor]) {

            statistik[buch.autor] = {
                gesamt: 0,
                ausgeliehen: 0
            };

        }

        statistik[buch.autor].gesamt++;

        if (buch.ausgeliehen) {
            statistik[buch.autor].ausgeliehen++;
        }

    }

    // Ergebnisarray erzeugen
    let ergebnis = [];

    for (let autor in statistik) {

        let quote =
            statistik[autor].ausgeliehen /
            statistik[autor].gesamt * 100;

        ergebnis.push({
            autor: autor,
            gesamt: statistik[autor].gesamt,
            ausgeliehen: statistik[autor].ausgeliehen,
            quote: quote
        });

    }

    return ergebnis;
}

console.log(getBorrowRateByAuthor())