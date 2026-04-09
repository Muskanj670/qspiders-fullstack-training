const user = {
  firstName: "Muskan",
  lastName: "Jain",
  age: 23,
  email: "muskanj@gmail.com",
  city: "Noida",
};

const keys = Object.keys(user);
console.log("Keys: ", keys);
const Values = Object.values(user);
console.log("Values: ", Values);

const entries = Object.entries(user);
console.log("Entries: ", entries);

const from_entries = Object.fromEntries(entries);
console.log("From Entries: ", from_entries);

console.log(Object.isFrozen(user));
Object.freeze(user); //No insertion, No deletion, NO updation
console.log(Object.isFrozen(user));

const company = {
  companyName: "ABC pvt ltd",
  location: "Noida",
};

const hiring = {
  designation: "Python Full Stack",
  CTC: "6LPA",
};

const emp = Object.assign({}, company, hiring, user);
console.log("Emp: ", emp);
