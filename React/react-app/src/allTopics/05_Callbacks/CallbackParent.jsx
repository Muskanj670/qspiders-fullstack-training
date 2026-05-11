import { useState } from "react";
import CallbackChild from "./CallbackChild"
const CallbackParent = () => {
    const [data, setData] = useState("")
    function getData(value) {
        setData(value)

    }
    return (
        <>
            <h1>Learn Callback in react</h1>
            <CallbackChild getData={getData} />
            <h2>Data from child to parent {data}</h2>
        </>
    )
}
export default CallbackParent