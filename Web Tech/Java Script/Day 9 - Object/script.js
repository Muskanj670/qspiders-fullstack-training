const emp = {
  firstNme: "Muskan",
  lastName: "Jain",
  email: "muskan@gmail.com",
  isWorking: false,
  getFullName: function () {
    console.log(`${this.firstNme} ${this.lastName}`);
  },
  greet: () => {
    console.log("Good Morning");
    return "Hello";
  },
};
console.log(emp);
console.log(emp.firstNme);
console.log(emp.lastName);
console.log(emp.getFullName());
console.log(emp.greet());

// ! Insertion
emp.city = "Noida";

// ! Updation
emp.isWorking = true;

// ! Deletion
delete emp.isWorking;

// ! In operator
console.log("isWorking" in emp);

// !Destructuring
// Object
const { firstNme, email } = emp;
console.log(firstNme);

// Array

const movies = ["3BHK", "PK", "KGF"];

const [m1, , m2] = movies;
console.log(m1);
console.log(m2);
