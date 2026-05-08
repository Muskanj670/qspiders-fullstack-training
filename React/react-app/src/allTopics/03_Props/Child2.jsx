const Child2 = (props) => {
    console.log(props);

    let { data1: str, data2: arr, data3: { name } } = props.data;
    console.log(str, arr, name);

    return (
        <>
            <h1>Child 2</h1>
        </>
    );
};

export default Child2;