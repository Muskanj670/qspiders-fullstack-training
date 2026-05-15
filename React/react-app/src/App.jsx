import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import FunctionBased from "./allTopics/01_Types-of-components/FunctionBased"
import ClassBased from "./allTopics/01_Types-of-components/ClassBased"
import StatesInFBC from "./allTopics/02_States/StatesInFBC"
import Heart from "./allTopics/02_States/Heart";
import Toggle from "./allTopics/02_States/Toggle";
import CounterFBC from "./allTopics/02_States/CounterFBC";
import StatesInCBC from "./allTopics/02_States/StatesInCBC";
import Parent from "./allTopics/03_Props/Parent1";
import DrillingParent from "./allTopics/04_PropsDrilling/DrillingParent";
import CallbackParent from "./allTopics/05_Callbacks/CallbackParent";
import UpliftingParent from "./allTopics/06_StateUplifting/UpliftingParent";
import UserLists from "./allTopics/07_Lists/UserLists";
import Employees from "./allTopics/07_Lists/Employees";
import ControlledForms1 from "./allTopics/08_ControlledForms/ControlledForms1";
import ControlledForms2 from "./allTopics/08_ControlledForms/ControlledForms2";
import InlineCSS from "./allTopics/09_ReactCSS/InlineCSS";
import Card from "./allTopics/09_ReactCSS/Card";

const App = () => {
    const username = 'Muskan';

    function greet() {
        return "Welcome";
    };
    return (
        <>
            {/* <Navbar />
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
            </table> */}
            {/* <FunctionBased />
            <ClassBased />
            <StatesInFBC />
            <Heart />
            <Toggle />
            <CounterFBC />
            <StatesInCBC />
            <Parent /> */}
            {/* <DrillingParent /> */}
            {/* <CallbackParent /> */}
            {/* <UpliftingParent /> */}
            {/* <UserLists /> */}
            {/* <Employees /> */}
            {/* <ControlledForms1 />
            <ControlledForms2 /> */}
            {/* <InlineCSS /> */}
            <Card />
            {/* <Footer /> */}
        </>
    );
}
export default App 