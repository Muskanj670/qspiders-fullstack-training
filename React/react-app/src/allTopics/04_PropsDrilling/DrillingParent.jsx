import { useState } from "react"
import Child from "./Child"

const DrillingParent = () => {
    let str = 'Hello'
    let arr = [10, 20]
    let obj = { username: "Muskan Jain" }
    let [data, setData] = useState("")
    let greet = () => setData("Hello");

    return (
        <>
            <hr />
            <h1>Drilling Parent {data}</h1>
            <Child str={str} arr={arr} obj={obj} greet={greet} />

        </>
    )
}

export default DrillingParent