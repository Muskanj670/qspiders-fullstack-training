const start = document.getElementById("start");
const stop = document.getElementById("stop");
const span = document.getElementById("count");

let count = 1;
let id ;
start.addEventListener("click",()=>{
    console.log("Start clicked");
    id = setInterval(() => {
        span.textContent = count++ ;
    },1)
});

stop.addEventListener("click",()=>{
    console.log("Stop clicked");
    clearInterval(id);
})

