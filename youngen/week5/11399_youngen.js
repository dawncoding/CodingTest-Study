var input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const [n, timeStr] = input //[5, '3 1 4 3 2']
const timeArr = timeStr.split(' ').map((time)=>+time)

const getData = () => {
return   timeArr.map((time,index)=>{
    return {
      who: index+1,
      time: time
    }
  })
}
const data = getData()
const sortedArr = data.sort((a,b)=>a.time - b.time)

let sum = 0 
const res = sortedArr.map((item)=>{
  sum = sum + item.time  
  return sum
})
const answer = res.reduce((acc,cur)=>acc+cur,0)
console.log(answer)
