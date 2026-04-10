// ! getElementById()

const heading = document.getElementById("heading");
heading.textContent = "Document Object Model (DOM)";
heading.style.color = "Red";
console.log("Heading: ", heading);

// ! getElementsByClassName()

const divRoot = document.getElementsByClassName("root");
console.log(divRoot);
divRoot[0].style.color = "blue";
divRoot[1].style.color = "red";
divRoot[2].style.color = "green";

// ! getElementsByTagName()

const divEle = document.getElementsByTagName("div");
console.log(divEle);

// ! querySelector()

const p2 = document.querySelector(".parent .p2");
p2.style.color = "Red";
const p4 = document.querySelector(".parent .p4");
p4.style.color = "Blue";

// ! querySelectorAll()
const paras = document.querySelectorAll("para");

