
const haystack: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
const needle: number = 5

function binarySearch(array: number[], x: number): number{
    let low: number = 0
    let high: number = array.length - 1
    while(low <= high){
        let mid: number = Math.floor((low + high) / 2)
        if(array[mid] < x){
            low = mid + 1
        }
        else if(array[mid] === x){
            return mid
        }
        else{
            high = mid - 1
        }
    }
    return -1
}

console.log(binarySearch(haystack, needle))