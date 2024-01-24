const fs = require('fs');
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");
const [n,...wordsArr] =input
let string = ''
wordsArr.forEach((item)=> string +=item)
const arr = [...string]
const result = {}
arr.forEach((char)=>{
  if(result[char]!==undefined){
    result[char] = result[char]+1
  } 
  if(result[char]===undefined) {
    result[char] = 1
  }
})
