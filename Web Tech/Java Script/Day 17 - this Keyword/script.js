/**
 * ! this in GEC
 */

console.log("this in GEC = ", this);

// ! this in regular function

function greet() {
  console.log("this in regular function", this);
}
greet();

// ! this in arrow function

const arrow = () => {
  console.log("this in arrow function", this);
};
arrow();

// ! this in regular method

const user = {
  firstName: "Muskan",
  lastName: "Jain",
  greet: function () {
    console.log("this in regular method", this);
  },
};

user.greet();

// ! this in arrow method

const user2 = {
  firstName: "Nancy",
  lastName: "Jain",
  greet: () => {
    console.log("this in arrow method", this);
  },
};

user2.greet();

// ! this in class

class Car {
  carName;
  carPrice;
  carColor;
  constructor(name, price, color) {
    console.log("this in class = ", this);
    this.carName = name;
    console.log("this in class = ", this);
    this.carPrice = price;
    console.log("this in class = ", this);
    this.carColor = color;
    console.log("this in class = ", this);
  }
}

const c1 = new Car("BMW", "2Cr", "Black");
console.log(c1);

// ! this in constructor function

function Car2(name, price, color) {
  console.log("this in constructor function = ", this);
  this.cName = name;
  this.cPrice = price;
  this.cColor = color;
  console.log("this in constructor function = ", this);
}

const c2 = new Car2("Fortuner", "80Lakh", "White");
console.log(c2);

// ! this in addEventListner's regular callback

const btn = document.getElementById('btn');
btn.addEventListener('click', function(){
    console.log("this in addEventListner's regular function = ",this);
})

// ! this in addEventListner's arrow callback

btn.addEventListener('click', () => {
    console.log("this in addEventListner's arrow function = ",this);
})

// ! this in nested regular method

const user3 = {
  firstName: "Ravi",
  lastName: "Jain",
  outer: function () {
    console.log("this in outer", this);
    function regularInner(){
        console.log("Regular Inner =  ",this)
    }

    const arrowInner = () =>{
        console.log("Arrow Inner = ", this);
    }
    regularInner();
    arrowInner();
  }
};

user3.outer()

