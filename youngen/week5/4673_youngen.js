const result = []
const range = Array.from({length : 10000},(num,index)=>index+1).map((num,index)=>index+1) //[1,2,...,10000]
function d(n){
  const arr = String(n).split('').reverse().map((num)=>+num)
let result = 0
  for(let i = 0 ; i < arr.length ; i++){
    result += arr[i] + arr[i]*10**i
}
return result
}
const notSelfArr = range.map((n)=>d(n))
const filteredArr = range.forEach((number)=>{
  if(!notSelfArr.includes(number)){
      result.push(number)
  }
})
console.log('result: ',result)
