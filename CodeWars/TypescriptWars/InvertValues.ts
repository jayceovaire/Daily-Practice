
// given an array of numbers, return an array of numbers with each value being inverted. [1, 2, 3] -> [-1, -2, -3]
export function invert(array: number[]): number[] {
    for(let i = 0; i < array.length; ++i){
        array[i] = array[i] * -1
    }

    return array
}