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


//Aufgabe 1.1
function showAllBooks(){
 for(let buch of buecher){
  console.log(buch.titel);
 }
}

showAllBooks()

// Aufgabe 1.2
function addBook(id,titel,autor,seiten){
 buecher.push({id,titel,autor,seiten,ausgeliehen:false});
}

addBook(11,"Beispielbuch","Mike Muster",100)

// Aufgabe 1.3
function findBookById(id){
 for(let buch of buecher){
  if(buch.id===id) return buch;
 }
 return null;
}

console.log(findBookById(1))

// Aufgabe 1.3
function averagePages(){
 let sum=0;
 for(let buch of buecher) sum+=buch.seiten;
 return sum/buecher.length;
}

console.log(averagePages())