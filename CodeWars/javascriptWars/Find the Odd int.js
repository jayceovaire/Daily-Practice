// Given an array of integers, find the one that appears an odd number of times.
// There will always be only one integer that appears an odd number of times.

function findOdd(array){
    const counts = {};
    for(let num of array){
        counts[num] = (counts[num] || 0) + 1
    }
    for(let num in counts){
        if (counts[num] % 2 === 1){
            return parseInt(num)
        }
    }
}