const fs = require('fs');
const input = fs.readFileSync("./input.txt").toString().trim().split("\n");
const [n,...wordsArr] =input
let string = ''
wordsArr.forEach((item)=> string +=item)
const arr = [...string]
let groupWordCount = 0


