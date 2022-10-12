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
  let url = 'https://catfact.ninja/fact';
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json;charset=utf-8',
    },
  });
  const data = await response.json();
  return data;
}

buttonElement.addEventListener('click', () => {
  promise.then(
    function (value) {
      let fact = getCatFact();
      console.log('response: ' + value);
      fact.then((response) => {
        console.log(response);
        outputElement.innerHTML = response.fact;
      });
    },
    function (error) {
      console.log('error');
    }
  );
});
