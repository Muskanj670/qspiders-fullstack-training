// ! Function Currying 

function outer(a){
    const inner = (b) =>{
        return a + b ;
    }
    return inner;
}

const res = outer(10)(20);
console.log("Res: ", res);

// ! Infinite Function Currying 

function outer2(a){
    const inner = (b) => {
        if (b === undefined){
            return a;
        }
        return outer2(a+b);
    }
    return inner;
}

const res2 = outer2(10)(20)(30)(40)(50)();
console.log("Res2: ", res2);