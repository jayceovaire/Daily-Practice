
// given an array of numbers, return the average of the numbers in the array.

export function findAverage(array: number[]): number {
    if (array.length == 0){
        return 0
    }
    else {
        let result: number = array.reduce((accumulator, iterator) => accumulator + iterator, 0)
        result = result / array.length

        return result
    }
}
