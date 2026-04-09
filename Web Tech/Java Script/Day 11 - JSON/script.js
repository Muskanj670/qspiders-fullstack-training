const obj = {
    firstname : 'Muskan',
    Lastname: 'Jain',
    email : 'Muskan@gmail.com',
    age : 23,
    isWorking : false
}

const jsonData = JSON.stringify(obj,null,4);
console.log(jsonData);

const parseData = JSON.parse(jsonData);
console.log(parseData);