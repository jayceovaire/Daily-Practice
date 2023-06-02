export function flattenAndSort(inputArray: number[][]): number[] {
    const flattenedArray = inputArray.flat()
    const sortedArray = flattenedArray.sort((a, b) => a - b);

    return sortedArray
}



console.log(flattenAndSort([[10, 2, 3, 7],[4, 5, 6,9]]))