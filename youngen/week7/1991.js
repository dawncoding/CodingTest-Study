const input = require('fs').readFileSync("youngen/input.txt").toString().trim().split('\n') 
console.log(input)
const [nodeAmount, ...arr] = input
