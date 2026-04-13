const dark = document.getElementById("dark");
const light = document.getElementById("light");
const body = document.body;

// ! Click

dark.addEventListener("click", () => {
  body.style.color = "White";
  body.style.backgroundColor = "black";
});

// ! Double Click

light.addEventListener("click", () => {
  body.style.color = "black";
  body.style.backgroundColor = "white";
});

// ! On Mouse Hover
const dark2 = document.getElementById("dark2");
const light2 = document.getElementById("light2");

dark2.addEventListener("mouseover", () => {
  body.style.color = "White";
  body.style.backgroundColor = "black";
});

light2.addEventListener("mouseover", () => {
  body.style.color = "black";
  body.style.backgroundColor = "white";
});

// ! mouseenter and mouseleave

const toggle = document.getElementById("toggle");
toggle.addEventListener("mouseenter", () => {
  body.style.color = "White";
  body.style.backgroundColor = "black";
});

toggle.addEventListener("mouseleave", () => {
  body.style.color = "black";
  body.style.backgroundColor = "white";
});
