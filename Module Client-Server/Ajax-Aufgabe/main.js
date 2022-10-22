const outputElement = document.querySelector('.output');
const buttonElement = document.querySelector('button');


let promise = new Promise(function (resolve, reject) {
  let x = 0;

  // The producing code (this may take some time)
  if (x == 0) {
    resolve('OK');
  } else {
    reject('Error');
  }
}); 

async function getCatFact() {

  // Your Code here



}

buttonElement.addEventListener('click', () => {

    // Your Code here







});
