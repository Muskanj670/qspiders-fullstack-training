const person = {
  name: "John",
  email: "john@gmail.com",
  age: 30,
  isWorking: true,
};

// ! Rest Operator in Object Destructuring
const { name, email, ...info } = person; //Rest operator should be the last always.
console.log(name);
console.log(email);
console.log(info);

// ! Rest operator in Array Destructuring
const skills = ["HTML", "css", "javascript", "react", "nodejs"];
const [skill1, skill2, ...restSkills] = skills;
console.log(skill1);
console.log(skill2);
console.log(restSkills);

// ! Spread Operator - to copy an object

const jack = {
  cake: "Black Forest",
  bike: "David Putra",
};
const oggy = { ...jack }; // This is a copy as it will copy all the property at the different memory location.
oggy.bike = "Pink Scooty";

const cockroach = { ...jack, cake: "Vanilla" };
console.log(jack);
console.log(oggy);
console.log(cockroach);

// ! Spread Operator in Array

const arr1 = [10, 20, 30, 40, 50];
const arr2 = [60, 70, 80, 90, 100];
const arr = [...arr1, ...arr2];
console.log(arr);

// ! Spread operator in nested objects

const jack2 = {
  cake: "Black Forest",
  bike: "David Putra",
  dialogue: {
    d1: "Tod dunga fod dunga",
    d2: "Papa",
  },
};

const oggy2 = { ...jack2, dialogue: { ...jack2.dialogue } };
oggy2.dialogue.d2 = "Olly";

console.log(jack2);
console.log(oggy2);

// ! Rest and spread operator in function
// ? Rest parameterized Regular named function

function sum(...args) {
  const total = args.reduce((acc, element) => acc + element, 0);
  return total;
}

const x = sum(1, 2, 3, 4, 5);
console.log("x: ", x);
