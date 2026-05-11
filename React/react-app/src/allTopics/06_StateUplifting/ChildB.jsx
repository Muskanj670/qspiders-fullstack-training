const ChildB = ({ setCount }) => {
    return (

        <>
            <h1>Child B</h1>
            <button onClick={() => setCount((prev) => prev + 1)}>Increment</button>
        </>
    )
}

export default ChildB