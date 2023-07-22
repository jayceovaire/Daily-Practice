// given an array of numbers return a new array containing only the even numbers

// brute force
export const getEvenNumbers = (numbersArray: number[]): number[] => {
    let evensArray: number[] = []
    for(let i = 0; i < numbersArray.length; i++){
        if(numbersArray[i] % 2 === 0){
            evensArray.push(numbersArray[i])
        }
    }

    return evensArray
}



// builtins
export const getEvenNumbers2 = (numbersArray: number[]): number[] => {
    return numbersArray.filter(num => num % 2 === 0)
}