
// Big O of Binary Search O(log n)
// Binary search can only be used on a sorted list

const haystack: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
const needle: number = 5

function binarySearch(array: number[], x: number): number{
    let low: number = 0
    let high: number = array.length - 1
    while(low <= high){
        let mid: number = Math.floor((low + high) / 2)
        let value = array[mid]
        if(value === x){
            return mid
        }
        else if(value < x){
            low = mid + 1
        }
        else{
            high = mid - 1
        }
    }
    return -1
}

console.log(binarySearch(haystack, needle)) // Returns index of needle in the haystack