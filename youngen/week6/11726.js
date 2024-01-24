const fs = require('fs');
const input = fs.readFileSync("./input.txt").toString().trim();
let n = +input
let a= 0
let b= 0
let sum = 0
let result = 1

function nPac (n){
  for(let i=1 ; i <= n ; i++){
    result = result * i
  }
  // console.log('result: ' ,result)
  return result
} //n!
while(b <= n){
  a = n- 2*b
  sum = sum + nPac(n) / nPac(a) * nPac(b)
  b++
  console.log('b',b)
  console.log('n',n)
}
// console.log(b)
// console.log('sum', sum)
// console.log(sum % 100
