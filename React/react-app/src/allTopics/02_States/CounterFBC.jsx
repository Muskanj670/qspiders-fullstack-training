import { useState } from "react";
const CounterFBC = () => {
    const [state, setState] = useState({ count: 0 })
    const updateState = () => setState({ count: state.count + 1 })
    return (
        <>
            <h1>CounterFBC Component {state.count}</h1>
            <button onClick={updateState}>Increment</button>
        </>
    )
}

export default CounterFBC;