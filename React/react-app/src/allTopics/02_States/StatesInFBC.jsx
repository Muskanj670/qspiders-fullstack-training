import { useState } from "react";

const StatesInFBC = () => {
    const [count, setCount] = useState(0);  // With the help of destructuring
    const incCount = () => setCount(count + 1);
    const decCount = () => { if (count > 1) { setCount(count - 1) } };
    const resetCount = () => setCount(0);

    return (
        <>
        <hr />
            <h2>Learn States in Function Based Components.</h2>
            <h2>Counter : {count}</h2>
            <button onClick={incCount}>Increment</button>
            <button onClick={decCount}>Decrement</button>
            <button onClick={resetCount} disabled={count === 0 ? true : false}>Reset</button>
            <hr />
        </>
    )
}

export default StatesInFBC

/**
 * ! What is state?
 * Im React state is a component's memory. It is an object used to store data that changes over time, such as user input, a shopping cart, or wheather a toggle is active.
 * 
 * ! What is useState ?
 * useState is a react hook that lets you add a state variable in your component.
 * 
 * ! How it works(The Syntax)
 * When you use it, you always returns an array consists of :
 *  - Th ecurrent value (what's currently in the memory box).
 *  - A function to update it (the tool to put something new in the box).
 */