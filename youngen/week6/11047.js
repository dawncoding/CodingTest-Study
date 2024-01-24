const fs = require('fs');
const input = fs.readFileSync("youngen/week6/input.txt").toString().trim().split("\n");

const [a, ...b] = input
const n = +a.split(' ')[0]
const k = +a.split(' ')[1]
const moneyVariables = b.map((item) => +item).reverse()
const moneyArr = [] //사용가능한 동전

for(let i = 0; i < n ; i++){
  if( k/ moneyVariables[i] >= 1){
    moneyArr.push(moneyVariables[i])
  }
}
let rest = k
let sum = 0
moneyArr.forEach((item)=>{
const gae = Math.floor(rest / item)
 rest = rest -  item * gae
 sum += gae
})
console.log(sum)
