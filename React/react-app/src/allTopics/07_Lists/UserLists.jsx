const UserLists = () => {
    const users = [
        { id: 1, name: "Allen" },
        { id: 2, name: "Bruce" },
        { id: 3, name: "Charlie" },
        { id: 4, name: "David" },
        { id: 5, name: "Eleven" }
    ]
    return (
        <>
            <h1>Learn Lists in React</h1>
            {
                users.map((user) => {
                    return (
                        <div key={user.id}>
                            <ol>
                                <li>{user.name}</li>
                            </ol>
                        </div>
                    )
                })
            }
        </>
    )
}

export default UserLists