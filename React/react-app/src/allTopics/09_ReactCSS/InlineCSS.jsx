const InlineCSS = () => {
    const subheadingStyle = {
        backgroundColor: "pink",
        color: "darkviolet"
    }
    return (
        <>
            <h1 style={{ backgroundColor: "crimson", color: "white" }}>Learn Inline CSS in React</h1>
            <h2 style={subheadingStyle}>This is subheading</h2>
        </>
    )
}

export default InlineCSS