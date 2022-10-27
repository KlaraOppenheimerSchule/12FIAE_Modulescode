function asynchFunktion(callbackFunction) {
    console.log('Hallo Welt');
    callbackFunction();
    console.log('Nach Hallo Welt und Callback');

}

function callbackFunction() {
    console.log('Ich bin der Callback');
}

asynchFunktion(callbackFunction);


