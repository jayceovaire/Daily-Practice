import {sumDigits} from "./summing absolute numbers";

export function switcheroo(x: string): string {
    let copyArray = x.split('')
    let newStr = ''
    for(let char of copyArray){
        if (char === 'a'){
            newStr += 'b'
        }
        if (char === 'b'){
            newStr += 'a'
        }
        if (char === 'c'){
            newStr += 'c'
        }
    }
    return newStr
}
