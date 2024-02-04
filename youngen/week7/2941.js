const fs = require('fs'); //dz=ak
const input = fs.readFileSync("youngen/input.txt").toString().trim()
const oldsArr = ['c=','c-','dz=','d-','lj','nj','s=','z=']
let count = 0
let word = input

for(let i = 0 ; i < oldsArr.length ; i++){
  if(input.includes(oldsArr[i])){
   
  } else continue
}