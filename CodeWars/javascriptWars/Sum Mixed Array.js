// Given an array of numbers and strings, return the sum of the array as
// if it were all numbers, as a number.

function sumMix(array) {
  const sum = array.reduce((accumulator, currentValue) => {
    return accumulator + Number(currentValue);
  }, 0);
  return sum;
}


