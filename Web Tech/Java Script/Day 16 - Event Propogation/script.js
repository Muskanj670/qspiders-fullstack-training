const grand = document.getElementById("grandparent");
const parent = document.getElementById("parent");
const child = document.getElementById("child");

grand.addEventListener(
  "click",
  () => {
    console.log("Grand Parent clicked ");
  },
  true,
);

parent.addEventListener(
  "click",
  () => {
    console.log("Parent clicked ");
  },
  true,
);

child.addEventListener(
  "click",
  (e) => {
    e.stopPropagation();
    console.log("Child clicked 1");
  },
  true,
);

child.addEventListener(
  "click",
  () => {
    console.log("Child clicked 2");
  },
  true,
);
