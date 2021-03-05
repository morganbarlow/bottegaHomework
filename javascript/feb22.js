const listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


// function JSExample (numbers) {
//   for (let num of numbers) { //the of prints out our numbers rather than their index
//     if (num === 3 || num === 7) { //we dont have and or an or we have && and, || or
//       console.log("ding!")
//     }
//     else {
//       console.log(num)
//     }
//   }
// }

function JSExample (numbers) {
  for (let i=0; i<numbers.length; i++) { // i stands for an iterator value, ++ is an incrimenter
    let num = numbers[i]
    if (num === 3 || num === 7) { //we dont have and or an or we have && and, || or
      console.log("ding!")
    }
    else {
      console.log(num)
    }
  }
}

JSExample(listOfNumbers)