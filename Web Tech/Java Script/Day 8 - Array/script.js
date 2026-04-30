// Initial Array
const arr = [10, 20, 30, 40, 50, 60];
console.log("Initial array: ", arr);

// ! 1. Push()
const a = arr.push(40);
console.log("a:", a);
console.log("After Push: ", arr);

// ! 2. pop()
const b = arr.pop();
console.log("b: ", b);
console.log("After Pop: ", arr);

// ! 3. Unshift()
const c = arr.unshift(0);
console.log("c: ", c);
console.log("After Unshift: ", arr);

// ! 4. shift()
const d = arr.shift();
console.log("d: ", d);
console.log("After shift: ", arr);

// ! 5. slice()
const e = arr.slice(0, 4);
console.log("e: ", e);
console.log("After slice: ", arr);

// ! 6. splice()
// * Insertion
const f = arr.splice(7, 0, 70, 80);
console.log("f: ", f);
console.log("After splice Insertion: ", arr);

// * Deletion
const g = arr.splice(6, 2);
console.log("g: ", g);
console.log("After splice deletion: ", arr);

// * Updation
const arr2 = [10, 200, 30];
console.log("Initial arr2: ", arr2);
const h = arr2.splice(1, 1, 20);
console.log("h: ", h);
console.log("After splice updation: ", arr2);

// ! 7. indexOf()
const arr3 = ["html", "css", "js", "react"];
console.log("Initial arr3", arr3);
const i = arr3.indexOf("js");
const i1 = arr3.indexOf("html", 1);
const j = arr3.indexOf("Angular");

console.log("index of js: ", i);
console.log("index of html from 1st index: ", i1);
console.log("index of Angular: ", j);

// ! 8. includes()
const k = arr3.includes("html");
const l = arr3.includes("Angular");
const m = arr3.includes("html", 1);

console.log("js in arr3: ", k);
console.log("Angular in arr3: ", l);
console.log("html in arr3 after 1st index: ", m);

// ! 9. reverse()
arr3.reverse();
console.log("arr3 after reverse: ", arr3);

// ! 10. sort()
arr3.sort();
console.log("arr3 after sort: ", arr3);

const arr4 = [4, 3545, 3654, 3257, 347];
console.log("Initial arr4:", arr4);
arr4.sort();
console.log("arr4 after sort:", arr4);

arr4.sort((a, b) => a - b);
console.log("arr4 after (a-b) callback: ", arr4);

arr4.sort((a, b) => b - a);
console.log("arr4 after (b-a) callback: ", arr4);

// ! 11. forEach()
const arr5 = [1, 2, 3, 4, 5];
console.log("Initial arr5: ", arr5);
const out = [];
arr5.forEach((element) => out.push(element * element));
console.log("out: ", out);

// ! 12. map()
const arr6 = [1, 2, 3, 4, 5];
console.log("Initial arr5: ", arr6);
const n = arr5.map((element) => element * 10);
console.log("n: ", n);

// ! 13. filter()

let filter_arr = [10, 20, 30, 40, 50];
const result = filter_arr.filter((element) => element > 25);
console.log("Filtered arr :", result);

// ! 14. reduce()

let reduce_arr = [10, 20, 30, 40, 50];
let reduce_res = reduce_arr.reduce((acc, ele) => acc + ele, 0);
console.log("Reduce: ", reduce_res);

// ! 15. reduceRight()

// ! 16. every()

const users = [
  { name: "Muskan", account: "Verifies" },
  { name: "Ravi", account: "Verifies" },
  { name: "Nancy", account: "Pending" },
];

const res = users.every((element) => {
  if (element.account === "Verifies") {
    return true;
  }
  return false;
});

console.log(res);

// ! 17. some()

const users2 = [
  { name: "Muskan", account: "Verifies" },
  { name: "Ravi", account: "Verifies" },
  { name: "Nancy", account: "Pending" },
];

const res2 = users2.some((element) => {
  if (element.account === "Verifies") {
    return true;
  }
  return false;
});

console.log(res2);

// ! 18. flat():
const nested_arr = [1, [2, 3], [4, [5, 6], 7], [8, [9, 10]]];
console.log("nested_arr = ", nested_arr);
console.log("After using flat: ", nested_arr.flat(2));

// ! 19. Array.isArray()
const variable = [1, 2, 3, [4, 5]];
const variable2 = 2;
console.log(Array.isArray(variable));
console.log(Array.isArray(variable2));

// ! 20. Array.from()

const st = "HTML";
console.log(Array.from(st));

// ! 21. find()
let find_arr = [10, 20, 30, 40, 50];
let find_result = find_arr.find((element) => element > 25);
console.log("Find :", find_result);

// ! 22. findIndex()

let find_index = [10, 20, 30, 40, 50];
let find_index_res = find_index.findIndex((element) => element > 25);
console.log("Find Index :", find_index_res);
