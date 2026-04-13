const E = document.querySelector("h3");
// ! Way 1

const changeText = () => {
  E.textContent = "hello";
};

const changeColor = () => {
  E.style.color = "red";
};

// ! Way 2

const btn1 = document.querySelector(".btn1");
btn1.onclick = () => {
  E.textContent = "Namaste Developers";
};

const btn2 = document.querySelector(".btn2");
btn2.ondblclick = () => {
  E.style.color = "blue";
};

// ! Way 3

const button1 = document.getElementById("btn1");
button1.addEventListener("click", () => {
  E.textContent = "Hello Developers";
});

const button2 = document.getElementById("btn2");
button2.addEventListener("dblclick", () => {
  E.style.color = "coral";
});
