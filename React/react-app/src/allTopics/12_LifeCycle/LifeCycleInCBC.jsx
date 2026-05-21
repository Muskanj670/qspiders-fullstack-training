import { Component } from "react";

export default class LifeCycleInCBC extends Component {
  constructor() {
    super();
    console.log("I am constructor");
    this.state = { count: 0 };
  }

  increment = () => this.setState({ count: this.state.count + 1 });
  componentDidMount() {
    console.log("I am componentDidMoun");
    this.intervalId = setInterval(() => {
      console.log("API Called");
    }, 2000);
  }

  componentDidUpdate() {
    console.log("Component Updated");
  }

  componentWillUnmount() {
    console.log("Component is goint to Unmount");
    clearInterval(this.intervalId);
  }
  render() {
    console.log("I am render");
    return (
      <>
        <h1>Count is {this.state.count}</h1>
        <button onClick={this.increment}>Increment</button>
      </>
    );
  }
}
