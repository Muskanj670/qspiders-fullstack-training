import { Component } from "react";
class StatesInCBC extends Component {
    constructor() {
        super();
        this.state = { data: "Hello World" };
    }
    updateState = () => {
        this.setState({ data: "Bye World!" })
    }
    render() {
        return (
            <>
                <h1>Learn States in FBC</h1>
                <h2>{this.state.data}</h2>
                <button onClick={this.updateState}>Click</button>
            </>
        );
    };
};

export default StatesInCBC;