const CallbackChild = ({getData} = props) => {
    let data = "Hello World"
    return (
        <>
            <h1>Callback child component</h1>
            <button onClick={() => getData(data)} >Click Me!</button>
        </>
    )
}
export default CallbackChild