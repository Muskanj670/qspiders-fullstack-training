import style from "./Card.module.css"
import { FaUser } from "react-icons/fa";
const Card = () => {
    return (
        <section id={style.cardContainer}>
            <div className={style.userImage}><FaUser /></div>
            <h1 className={style.userName}>Muskan Jain</h1>
            <p className={style.desig}>Full stack developer</p>
            <p className={style.description}>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sit beatae explicabo deleniti quibusdam officia consequuntur.</p>
            <button className={style.btn}>Hire Me!</button>
        </section>
    )
}
export default Card