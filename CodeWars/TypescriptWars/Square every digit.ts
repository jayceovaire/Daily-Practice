// given a number, square every number in that number and return it as a new number with each number joined
// example 812 = 8*8 1*1 2*2
// example 64 1 4
// return 6414

export class Kata {
    static squareDigit(num: number): number {
        let new_digit = ''
        let string_num = num.toString().split('')

        for (let i = 0; i < string_num.length; i++){
            const n = Number(string_num[i]) * Number(string_num[i])
            new_digit += String(n)

        }
        return Number(new_digit)
    }
}



