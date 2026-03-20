// Var examples
var a;
console.log("a:", a); // Output: undefined
var a = 10;
var a = 20;
var a = 30;

console.log("a:", a); // Output: 30
a = 40;
console.log("a:", a); // Output: 40
var a;
console.log("a:", a); // Output: 40

// Let examples
let b;
console.log("b:", b); // Output: undefined
/**
 * !⚠️The following lines will throw an error because 'let' does not allow redeclaration of the same variable within the same scope.
 * ! let b = 10;
 */

b = 20;
console.log("b:", b); // Output: 20
b = 30;
console.log("b:", b); // Output: 30

// Const examples
const c = 10;
console.log("c:", c); // Output: 10
/** 
 * !⚠️The following lines will throw an error because 'const' does not allow reassignment of the variable after it has been initialized.
 * ! c = 20;
 */