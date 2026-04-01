// Initial Array
const arr = [10,20,30,40,50,60]
console.log("Initial array: ",arr)

// ! 1. Push()
const a = arr.push(40)
console.log("a:",a)
console.log("After Push: ",arr)

// ! 2. pop()
const b = arr.pop()
console.log("b: ",b)
console.log("After Pop: ",arr)

// ! 3. Unshift()
const c = arr.unshift(0)
console.log("c: ",c)
console.log("After Unshift: ",arr)

// ! 4. shift()
const d = arr.shift()
console.log("d: ",d)
console.log("After shift: ",arr)

// ! 5. slice()
const e = arr.slice(0,4)
console.log("e: ",e)
console.log("After slice: ",arr)

// ! 5. splice()
    // * Insertion
        const f = arr.splice(7,0,70,80)
        console.log("f: ",f)
        console.log("After splice Insertion: ",arr)

    // * Deletion
        const g = arr.splice(6,2)
        console.log("g: ",g)
        console.log("After splice deletion: ",arr)


    // * Updation
        const arr2 = [10,200,30]
        console.log("Initial arr2: ",arr2)
        const h = arr2.splice(1,1,20)
        console.log("h: ",h)
        console.log("After splice updation: ",arr2)


