const Child =(props) =>{
    return(
        <>
        <h1>Hello from Child</h1>
        <h2>{props.prop1}, {props.prop2}</h2>
        </>
    )
}

export default Child;