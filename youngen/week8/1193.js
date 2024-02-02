const fs = require('fs');
const input = +fs.readFileSync("youngen/input.txt").toString()
let n, rest
for(let i = 1; i <= input ; i++){
  if(i*(i+1)/2 >= input){
    n = i-1
rest = input - n*(n+1)/2
break}}
if(n % 2 !== 0){
  console.log( `${rest}/${n-rest+2}`) 
}
if(n % 2 === 0){
  console.log( `${n-rest+2}/${rest}`)
}
  


