const input = require('fs').readFileSync("youngen/input.txt").toString().trim().split('\n') 
const [n,...rest] = input
console.log(rest)
const numberArr = rest.map((item)=>+item)
const arr = []
for(let i = 0; i < numberArr.length; i++){
  if(numberArr[i] === 0){
    if(arr.length === 0){
      console.log(0)
    }
    else {
      arr.sort((a,b)=> a-b)
      console.log(arr[arr.length-1])
      arr.pop()
    }
  }
  else {
    arr.push(numberArr[i])
  }
}