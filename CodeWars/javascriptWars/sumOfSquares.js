// Given an array of numbers, return the sum of all numbers after they have been squared.

function squareSum(numbers){
    let copy = numbers.slice()
    let sumList = []
    for (let i = 0; i < copy.length; i++){
        let result = copy[i] * copy[i]
        sumList.push(result)
    }
    let final = 0
    for(let i = 0; i < sumList.length; i++){
         final += sumList[i]
    }
    return final
}

// ____________________________Solve 2_______________________________________
function squareSum2(numbers){
    let copy = numbers.slice()
    return copy.reduce((sum, number) => (sum + (number * number), 0))
}

// ____________________________Recursive Solve______________________________________

function squareSumRec(numbers){
    let copy = numbers.slice()
    if(copy.length === 0){
        return 0
    }
    else{
        const lastNum = copy[copy.length - 1]
        const sumOfSquares = squareSumRec(copy.slice(0,-1))
        return sumOfSquares + (lastNum * lastNum)
    }
}