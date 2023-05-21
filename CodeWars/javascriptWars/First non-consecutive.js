
// given a list of numbers check to make sure they are all consecutive, if they are all consecutive
// return null, if they are not return the first non-consecutive number


function firstNonConsecutive(arr){
    for (let i = 1; i < arr.length; i++){
        if(arr[i] - arr[i - 1] !== 1){
            return arr[i]
        }
    }
    return null
}

console.log(firstNonConsecutive([1,2,3,8,5,6,7]))