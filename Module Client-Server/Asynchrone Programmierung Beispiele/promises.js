
let myPromise = new Promise(function(resolve, reject) {
    let x = 0;
  
    if (x == 0) {
      resolve("OK");
    } else {
      reject("Error");
    }
  });
  
  myPromise.then(

    function successValue(result) {
      console.log(result);
    },
  )

  .catch(

    function errorValue(result) {
      console.log(result);
    }

  );


  console.log('Hier geht es um Promises');



