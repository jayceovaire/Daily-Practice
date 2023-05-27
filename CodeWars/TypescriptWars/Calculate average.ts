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