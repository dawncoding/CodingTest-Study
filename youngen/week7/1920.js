const fs = require('fs');
const input = fs.readFileSync("youngen/input.txt").toString().trim().split("\n");
const [n, stringN, m, stringM] = input
const arrN = stringN.split(' ')
const arrM = stringM.split(' ')
arrM.forEach((m)=>{
  if(arrN.includes(m)){
    console.log(1)
  } else {console.log(0)}
})