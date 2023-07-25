export function pipeFix(numbers: number[]): number[] {
    let firstIndex = numbers[0]
    let highestValue = numbers[0]
    let result = []
    for(let i = 0; i < numbers.length; i++){
        if(numbers[i] > highestValue){
            highestValue = numbers[i]
        }
    }
    while (firstIndex <= highestValue){
        result.push(firstIndex)
        firstIndex ++
    }
    
    return result
}