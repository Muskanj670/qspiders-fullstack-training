console.log("Start");
var a = 10;
let b = 20;
{
  var a = 100;
  let b = 200;

  {
    var c = 100;
    let d = 200;
    console.log("Inside block 2");
    console.log("a:", a);
    console.log("b:", b);
    console.log("c:", c);1
    console.log("d:", d);
  }
  console.log("Inside block 1");
  console.log("a:", a);
  console.log("b:", b);
  console.log("c:", c);
}
console.log("Outside");
console.log("a:", a);
console.log("b:", b);
console.log("c:", c);
