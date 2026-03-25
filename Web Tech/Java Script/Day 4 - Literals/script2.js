
const num1 = +prompt("Enter a num1: ");
const num2 = +prompt("Enter num2:" );
const num3 = +prompt("Enter 3rd num: ")
const res = num1 > num2 && num1 > num3 ? num1 : num2 > num3? num2 : num3;
console.log(`Bigger no is : ${res}`)