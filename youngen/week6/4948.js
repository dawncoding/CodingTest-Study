const input = require('fs').readFileSync("youngen/week6/input.txt").toString().trim().split('\n') 
const numbers = input.map((item)=>+item)
const getDivisors = (number) => {
  const divisors = []
  let i = 1
  while(i <= number/2){
    if(Number.isInteger(number/i)){
      divisors.push(i)
    }
    i++
  }
  return [...divisors,number]
}
numbers.forEach((number)=>{
  let sum = 0
  // 시작이 홀수일 때 
  if(Number.isInteger(number/2)){
    for(let i = number+1 ; i <= number*2 ; i+=2){
      if(getDivisors(i).length===2){
        sum = sum +  1
      }
    }
  } else {
    //시작이 짝수일 때
    for(let i = number+1 ; i <= number*2 ; i++){
      if(getDivisors(i).length===2){
        sum = sum +  1
      }
    }
  }
  if(sum)console.log(sum)
})