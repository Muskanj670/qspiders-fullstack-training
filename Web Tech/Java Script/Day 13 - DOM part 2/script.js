// ! Document.createElement()

const h1 = document.createElement("h1");
h1.textContent = "Hello from JS";
const root = document.getElementById("root");

// ! parent.appendChild()
root.appendChild(h1);

const p1 = document.createElement("p");
const p2 = document.createElement("p");
p1.textContent = "Paragraph 1";
p2.textContent = "Paragraph 2";

// ! parent.appendChild()
root.append(p1, p2);

const innerHTML = document.getElementById("innerHTML");
innerHTML.textContent = "<h1>Heading 1</h1>";
innerHTML.innerHTML = "<h1>Heading 1</h1>";

const atbt = root.getAttribute("id");
const atbt2 = root.getAttribute("class");

console.log(atbt);
console.log(atbt2);

root.setAttribute("class", "container")
const atbt3 = root.getAttribute("class");
console.log(atbt3);

root.removeAttribute("class");
const atbt4 = root.getAttribute("class");
console.log(atbt4);



