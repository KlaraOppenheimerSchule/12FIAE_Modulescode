async function getUsers() {

    const response = await fetch(
        "https://jsonplaceholder.typicode.com/users"
    );

    return await response.json();

}


// Aufruf
async function main() {
    const users = await getUsers();
    console.table(users);
}

main()