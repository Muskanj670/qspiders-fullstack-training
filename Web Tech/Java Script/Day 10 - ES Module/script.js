/**
 * !Program 1
 */
import sum from "./A.js"; // default import
import { mul, sub } from "./B.js"; // named import
console.log("--------Program 1----------\n\n");
console.log("Sum = ", sum(10, 2));
console.log("Mul = ", mul(10, 2));
console.log("Div = ", sub(10, 2));

/**
 * !Program 2
 */
import { fname, email } from "./A.js";
import city from "./B.js";
console.log("--------Program 2----------\n\n");

console.log("FirstName = ", fname);
console.log("Email = ", email);
console.log("City = ", city);
