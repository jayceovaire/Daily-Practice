export function sumDigits(n: number): number{

    let stringedNum = Math.abs(n).toString().split('')
    let absolute: number = 0
    for (let num of stringedNum){
        absolute += +num
    }

    return absolute
}

console.log(sumDigits(-32))


export function sumDigits2(n: number): number{
    return Math.abs(n).toString().split('').reduce((acc, iter) => +iter + acc,0)
}