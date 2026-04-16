const p1 = {
  firstName: "Virat",
  lastName: "Kohli",
  team: "RCB",
};

function stats(jersy, val) {
  console.log(this);
  console.log("Jersy No ", jersy);
  console.log("is Orange cap holder ", val);
}

stats.call(p1, 18, true);
stats.apply(p1, [18, true]);
const res = stats.bind(p1, 18, true);

setTimeout(() => {
  res();
}, 3000);
