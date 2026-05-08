import Child from "./Child1";
import Child2 from "./Child2";
import Child3 from "./Child3";
const Parent = () => {

    let data1 = "Hello";
    let data2 = [10, 20, 30];
    let data3 = { name: "Muskan" }
    return (
        <>
            <h1>Hello from Parent</h1>
            <Child prop1={data1} prop2={data2} prop3={data3} />
            <Child2 data={{ data1, data2, data3 }} />
            <Child3 prop1={data1} prop2={data2} prop3={data3} />
        </>
    )
}

export default Parent;