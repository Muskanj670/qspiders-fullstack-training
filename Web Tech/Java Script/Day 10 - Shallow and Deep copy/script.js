const jack = {
  cake: "Black Forest",
  bike: "David Putra",
};

// !Shallow Copy

const oggy = jack; // This is not a copy, it's a reference to the same object in memory
oggy.cake = "Vanilla"; // This will change the cake property for both oggy and jack, because they reference the same object.
console.log(jack.cake); //Output: Vanilla

// !Deep Copy

const oggy2 = structuredClone(jack); // This is a copy as it will copy all the property at the different memory location.
oggy2.cake = "Strawberry";
console.log(jack.cake); // Output: Vanilla
console.log(oggy2.cake); // Output: Strawberry
