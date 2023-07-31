export function findUniq(arr: number[]): number {

    let i = 0
    let first = arr[0]
    if (arr[0] === arr[1]){
        first = arr[0]
    }
    else if (arr[0] !== arr[1] && arr[0] === arr[2]){
        return arr[1]
    }
    else if (arr[0] !== arr[1] && arr[0] !== arr[2]){
        return arr[0]
    }
    for (i; i < arr.length; i++){
            if (arr[i] !== first){
                return arr[i]
            }
        }
    
    return -1
}