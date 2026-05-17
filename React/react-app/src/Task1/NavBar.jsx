import style from "./NavBar.module.css"
import { IoFileTrayOutline, IoTvSharp, IoFastFoodOutline } from "react-icons/io5";
import { FaMobileScreen } from "react-icons/fa6";
import { FaTshirt, FaBook } from "react-icons/fa";
import { GiLipstick, GiFullMotorcycleHelmet, GiScooter, GiSofa } from "react-icons/gi";
import { ImPrinter } from "react-icons/im";
import { LuLamp } from "react-icons/lu";
// import { IoTvSharp } from "react-icons/io5";
import { RiBearSmileFill } from "react-icons/ri";
// import { IoFastFoodOutline } from "react-icons/io5";
import { TbCricket } from "react-icons/tb";
const NavBar = () => {
    return (
        <nav>
            <a href="#"><IoFileTrayOutline />For You</a>
            <a href="#"><FaTshirt />Fashion</a>
            <a href="#"><FaMobileScreen />Mobiles</a>
            <a href="#"><GiLipstick />Beauty</a>
            <a href="#"><ImPrinter />Electronics</a>
            <a href="#"><LuLamp />Home</a>
            <a href="#"><IoTvSharp />Appliances</a>
            <a href="#"><RiBearSmileFill />Toys</a>
            <a href="#"><IoFastFoodOutline />Food</a>
            <a href="#"><GiFullMotorcycleHelmet />Auto</a>
            <a href="#"><GiScooter />2 Wheelers</a>
            <a href="#"><TbCricket />Sports</a>
            <a href="#"><FaBook />Books</a>
            <a href="#"><GiSofa />Furniture</a>
        </nav>
    )
}

export default NavBar