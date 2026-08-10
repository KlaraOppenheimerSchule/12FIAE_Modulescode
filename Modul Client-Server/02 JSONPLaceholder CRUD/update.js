// alles ändern
async function updateUser(id, name, email) {

    const response = await fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`,
        {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id: 1,
                name: name,
                email: email
            })
        }
    );

    return await response.json();

}

// ein Merkmal ändern
async function patchUser(id,email) {

    const response = await fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`,
        {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email
            })
        }
    );

    return await response.json();

}


// Aufrufen
async function main() {

    

    console.log("===== PUT =====");

    const updatedUser = await updateUser(1,"Max Muster","neu@test.de");
    console.log(updatedUser);

    console.log("===== PATCH =====");

    const patchedUser = await patchUser(1,"noch-neuer@test.de");
    console.log(patchedUser);

}

main()