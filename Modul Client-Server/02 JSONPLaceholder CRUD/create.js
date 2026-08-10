async function createUser(name,email) {

    const response = await fetch(
        "https://jsonplaceholder.typicode.com/users",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                email: email
            })
        }
    );

    return await response.json();

}


// Aufrufen
async function main() {
    const newUser = await createUser("Max Mustermann","max@test.de");
    console.log(newUser);
}

main();
