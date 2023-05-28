
// given a string of numbers return the numbers as a binary, for every number in the string if it is 5 or higher
// return a 1, if 4 or lower return a 0
// the returned value should be a string.

export const fakeBin = (x: string): string => {
    let result: string[]  = []
    for(let i = 0; i < x.length; i++){
        if('56789'.includes(x[i])){
            result.push('1')
        }
        else {
            result.push('0')
        }
    }
    return result.join('')
}

export const fakeBin2 = (x: string): string => {
    let result: string[] = []
    for (let i = 0; i < x.length; i++){
        switch (x[i]){
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                result.push('1')
                break
            default:
                result.push('0')
                break
        }
    }
    return result.join('')
}