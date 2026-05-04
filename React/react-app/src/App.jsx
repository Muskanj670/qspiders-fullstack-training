import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
const App = () =>{
    const username = 'Muskan';

    function greet(){
        return "Welcome";
    };
    return (
    <>
        <Navbar/>
        <h1>I am App component(Parent)</h1>
        <h2>{greet()} {username}</h2>
        <hr />
        <div style={{ textAlign: "center", margin: "1rem 0" }}>
            <strong>Types of Components</strong>
        </div>
        <table border={2}>
            <thead>
                <tr>
                    <th>ClassBased Comp</th>
                    <th>Function Based Comp</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>JS classes</td>
                    <td>JS Functions</td>
                </tr>
                <tr>
                    <td>StateFull</td>
                    <td>Stateless</td>
                </tr>
                <tr>
                    <td>No Hooks</td>
                    <td>Hooks</td>
                </tr>
                <tr>
                    <td>Life cycle Methods</td>
                    <td>No Life cycle methods</td>
                </tr>
                <tr>
                    <td>'this' keyword</td>
                    <td>No 'this' keyword</td>
                </tr>
            </tbody>
        </table>

        <Footer/>
    </>
    );
}
export default App 