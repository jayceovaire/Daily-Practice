
// Complete the function that takes a non-negative integer n as input,
// and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive )

export function powersOfTwo(n: number): number[]{
    let result: number[] = []
    let i: number = 0
    while (i <= n){
        result.push(2 ** i)
        i++
    }

    return result
}