const NestedChild = ({ props }) => {
    let { str, arr, obj: { username }, greet } = props
    return (
        <>
            <hr />
            <h1>Nested Child</h1>
            <h2>{str}, {username} </h2>
            <p>{arr}</p>
            <button onClick={greet}> Click Me! </button>
        </>
    )
}

export default NestedChild