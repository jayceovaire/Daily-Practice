//Given a list of integers, determine whether the sum of its elements is odd or even.
// Give your answer as a string matching "odd" or "even".
// If the input array is empty consider it as: [0] (array with a zero).

function oddOrEven(array){
    //checks to make sure input is an array and that it is not empty
    if(!Array.isArray(array) || array.length === 0){
        return 'even';
    }
    let copy = array.slice();
    // copies array then checks to make sure it is longer than 1, or that if length is 1 that value is not 0
    if(copy.length === 1 && copy[0] === 0){
        return 'even';
    }
    //reducer sums all numbers in list then we use modulus 2 to check for odd or even
    let result = copy.reduce((acc, val) => acc + val, 0);
    return result % 2 === 0 ? 'even' : 'odd';
}

