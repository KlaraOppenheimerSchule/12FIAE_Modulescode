//Here we are fetching a JSON file across the network, parsing it, and printing the data to the console.
//The simplest use of fetch() takes one argument — the path to the resource you want to fetch — 
//and does not directly return the JSON response body but instead returns a promise that resolves 
//with a Response object.

//The Response object, in turn, does not directly contain the actual JSON response body but 
//is instead a representation of the entire HTTP response. So, to extract the JSON body content 
//from the Response object, we use the json() method, which returns a second promise that resolves 
//with the result of parsing the response body text as JSON.))

//https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

async function getTodos() {
  try{
    const response = await fetch ("https://jsonplaceholder.typicode.com/todos/1")
    const data = await response.json()
    console.log(data)
  }
  catch (err) {
    console.log("Something went wrong...")
    console.log(err)
  }
}

getTodos()