/* FInde Duplikate - Fehlerhaft

function findDuplicates() {
    const numbers = [2, 4, 5, 2, 5, 8, 5, 10];
    for(let i=0; i<numbers.length; i++){
        const numberAtI = numbers[i];
        for(let j=0; j<numbers.length; j++) {
            const numberAtJ = numbers[j];
            if(numberAtI === numberAtJ) {
                console.log(`Doppelte Zahl gefunden:${numberAtI}`);
            }
        }
    }
}

findDuplicates(); */

//Finde Duplikate korrekt 

function findDuplicates() {
    const numbers = [2, 4, 5, 2, 5, 8, 5, 10];
    for(let i=0; i<numbers.length; i++){
        const numberAtI = numbers[i];
        for(let j=i+1; j<numbers.length; j++) {
            const numberAtJ = numbers[j];
            if(numberAtI === numberAtJ) {
                console.log(`Doppelte Zahl gefunden:${numberAtI}`);
            }
        }
    }
}

findDuplicates(); 

// Beispiel
/*
let x = 19.00 + "Hallo 12. Klasse" + 4;
console.log(x);

const student = {
    name:"Max Schmied", 
    klasse:"12FIx", 
    alter:"19"
};

console.log(`Der Schüler heisst ${student.name}`); */



const promise = new Promise(function (resolve, reject) {
	const x = "12 Klasse ist super";
	const y = "12 Klasse ist super";
	if (x === y) {
	resolve();
	} else {
	reject();
	}
});

promise
	.then(function () {
	console.log("Promise war erfolgreich!");
	})
	.catch(function () {
	console.log("Promise wurde zurückgewiesen!");
	});

