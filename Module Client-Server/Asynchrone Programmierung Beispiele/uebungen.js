function textOne() {
    console.log('Ich geh mit meiner Laterne ...');
   }
   
   function textTwo() { 
       console.log('.. und meine Laterne mit mir!');
   }
   
   function textThree() { 
       console.log('Da oben leuchten die Sterne ... ');
   }
   
   function main() {
     setTimeout(textOne, 60);
     setTimeout(textThree, 20);
   
     new Promise((resolve, reject) =>
       resolve('... und unten leuchten wir!')
     ).then(resolve => console.log(resolve));
       
     new Promise((resolve, reject) =>
       resolve('ENDE')
     ).then(resolve => console.log(resolve));
   
     textTwo();
   }
   
   main();