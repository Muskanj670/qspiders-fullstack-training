import { useState } from "react";

const Heart = () => {
    const [likes, setLikes] = useState(0);

    const updateLikes = () => {
        // setLikes(likes + 1);
        // setLikes(likes + 1);
        // setLikes(likes + 1);

        setLikes((prev) => prev + 1);
        setLikes((prev) => prev + 1);
        setLikes((prev) => prev + 1);

    }

    return (
        <>
            <span onClick={updateLikes}>❤</span><sup>{likes}</sup>
            <hr />
        </>
    )
}

export default Heart;