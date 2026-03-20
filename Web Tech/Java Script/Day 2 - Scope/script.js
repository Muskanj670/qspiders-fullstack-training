var a = 10;
let b = 20;
const c = 30;
console.log('a:', a);
console.log('b:', b);
console.log('c:', c);
console.log(window.a); // 10
console.log(window.b); // undefined
console.log(window.c); // undefined
console.log(globalThis.a); // 10
console.log(globalThis.b); // undefined     