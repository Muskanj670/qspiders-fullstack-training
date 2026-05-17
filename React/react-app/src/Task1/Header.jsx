import { SiFlipkart } from "react-icons/si";
import { GiScooter } from "react-icons/gi";
import { BsFillAirplaneEnginesFill } from "react-icons/bs";
import { FaLocationDot } from "react-icons/fa6";
import { TbCoinRupeeFilled } from "react-icons/tb";
import { CiSearch } from "react-icons/ci";
import { FaRegUserCircle } from "react-icons/fa";
import { IoCartOutline } from "react-icons/io5";
import { IoIosArrowForward } from "react-icons/io";
import { IoIosArrowDown } from "react-icons/io";
import style from './Header.module.css'
const Header = () => {
    return (
        <header>
            <div className={style.upper}>
                <div className={style.left}>
                    <div className={style.box} id={style.logo}>
                        <span><SiFlipkart />Flipkart</span>
                    </div>
                    <div className={style.box}>
                        <span><GiScooter />Minutes</span>
                    </div><div className={style.box}>
                        <span><BsFillAirplaneEnginesFill />Travel</span>
                    </div>
                </div>
                <div className={style.right}>
                    <div className={style.location}>
                        <p>
                            <FaLocationDot /> Location not set <span>Select delivery location <IoIosArrowForward /> </span>
                        </p>
                    </div>
                    <div className={style.coins}>
                        <span><TbCoinRupeeFilled />0</span>
                    </div>
                </div>
            </div>
            <div className={style.lower}>
                <div className={style.searchBar}>
                    <CiSearch />
                    <input type="text" name="" id="" placeholder="Search for products, brands and More" />
                </div>
                <div className={style.userContainer}>
                    <div className={style.user}><FaRegUserCircle /> Muskan <IoIosArrowDown /></div>
                    <div className={style.user}>More <IoIosArrowDown /></div>
                    <div className={style.user}><IoCartOutline />Cart</div>

                </div>
            </div>
        </header>
    )
}

export default Header