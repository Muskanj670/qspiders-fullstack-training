const inp1 = document.getElementById("inp1")

const callAPI = (val) =>{
    console.log("Api called for ", val);
}

inp1.addEventListener('input',(e) =>{
    callAPI(e.target.value);
})