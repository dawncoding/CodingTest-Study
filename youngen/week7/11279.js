const input = require('fs').readFileSync("youngen/input.txt").toString().trim().split('\n') 
const [n,...rest] = input
const numberArr = rest.map((item)=>+item)
const arr = []
for(let i = 0; i < n; i++){
  if(numberArr[i] === 0){
    if(arr.length === 0){
      console.log(0)
    }
    if(arr.length !== 0) {
      arr.sort((a,b)=> a-b)
      console.log(arr[arr.length-1])
      arr.pop()
    }
  }
  if(numberArr[i]!==0) {
    arr.push(numberArr[i])
  }
}