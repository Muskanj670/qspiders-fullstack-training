import { useState } from "react";

const ToggleComponent = () => {
    const [toggle, setToggle] = useState(false);

    return (
        <>
            <button onClick={() => { setToggle((prev) => !prev) }}>Toggle Me!</button>
            {toggle && <h1>Toggle Example</h1>}
        </>
    )
}

export default ToggleComponent;