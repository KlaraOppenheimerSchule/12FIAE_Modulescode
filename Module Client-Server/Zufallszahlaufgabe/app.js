function randomNumberOne() {
	return new Promise(resolve => {
		setTimeout(() => {
			const x = Math.floor(Math.random()*10)+1;
			resolve(x);
		}, 4000);
	})
}

function randomNumberTwo() {
	return new Promise(resolve => {
		setTimeout(() => {
			const x = Math.floor(Math.random()*10)+1;
			resolve(x);
		}, 6000);
	})
}

async function firstFunction() {
	
	
	const a = await randomNumberOne();
	const b = await randomNumberTwo();
	
	console.log(`Das Ergbnis ist 1. Funktion ist ${ a * b}`);
}

async function secondFunction() {
	
	
	const a = await randomNumberOne();
	const b = await randomNumberOne();
	
	console.log(`Das Ergbnis ist der 2. Funktionen ist ${ a * b}`);
}

firstFunction();
secondFunction();