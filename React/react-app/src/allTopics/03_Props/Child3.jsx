const Child3 = ({ prop1, prop2, prop3: { name } }) => {
    return (
        <>
            <hr />
            <h1>Child 3</h1>
            <h2>{prop1}, {name}</h2>
            <p>{prop2}</p>
        </>
    )
}

export default Child3