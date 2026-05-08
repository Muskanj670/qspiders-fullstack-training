import NestedChild from "./NestedChild"

const Child = (props) => {
    console.log(props);

    return (
        <>
            <hr />
            <h1>Child</h1>
            <NestedChild props={props} />
        </>
    )
}

export default Child