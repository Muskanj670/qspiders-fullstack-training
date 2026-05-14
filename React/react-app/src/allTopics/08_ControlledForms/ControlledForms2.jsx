import { useState } from "react"

const ControlledForms2 = () => {

    const [FormData, setFormData] = useState({
        username: "",
        email: "",
        password: ""
    })

    const HandleFormData = (e) => {
        let { name, value } = e.target
        setFormData({ ...FormData, [name]: value })
    }

    const HandleSubmit = (e) => {
        e.preventDefault()
        console.log(FormData);

        let existingUsers = JSON.parse(localStorage.getItem("users")) || []
        existingUsers.push(FormData)
        localStorage.setItem("users", JSON.stringify(existingUsers))
        alert("User Created successfully....")
        setFormData({ username: "", email: "", password: "" })

    }
    return (
        <>
            <h1>Learn Controlled Forms 2</h1>
            <p>Handle multiple inputs using states</p>

            <form onSubmit={HandleSubmit}>
                <label htmlFor="username">Username: </label>
                <input type="text" name="username" id="username" value={FormData.username} onChange={HandleFormData} />
                <br />

                <label htmlFor="email">Email: </label>
                <input type="email" name="email" id="email" value={FormData.email} onChange={HandleFormData} />
                <br />

                <label htmlFor="password">Password: </label>
                <input type="password" name="password" id="password" value={FormData.password} onChange={HandleFormData} />
                <br />

                <button>Submit</button>
            </form>
        </>
    )
}

export default ControlledForms2