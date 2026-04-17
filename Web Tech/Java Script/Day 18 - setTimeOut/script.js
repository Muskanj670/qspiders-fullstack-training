console.log("start")

setTimeout(()=>{
    console.log("TASK - 1")
},5000)

setTimeout(()=>{
    console.log("TASK 2")
    clearTimeout(id)
},2000)

const id = setTimeout(()=>{
    console.log("TASK - 3")
},3000)

console.log("Stop")