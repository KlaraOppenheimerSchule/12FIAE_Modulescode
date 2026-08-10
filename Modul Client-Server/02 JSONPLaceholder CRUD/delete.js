async function deleteUser(id) {

    const response = await fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`,
        {
            method: "DELETE"
        }
    );

    return response.ok;

}

// Aufrufen
async function main() {

    const deleted = await deleteUser(1);
    console.log(deleted);

}

main()