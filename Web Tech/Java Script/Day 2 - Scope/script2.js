console.log("Start");
var a = 10;
let b = 20;
const c = 30;

{
  var a = 100;
  let b = 200;
  const c = 300;
  var d = 400;
  console.log("Inside a block..");
  console.log("a:", a);
  console.log("b:", b);
  console.log("c:", c);
  console.log("d:", d);
}
console.log("Outside a block");
console.log("a:", a);
console.log("b:", b);
console.log("c:", c);
console.log("d:", d);
console.log("End");
