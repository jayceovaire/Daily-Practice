
// write a function that checks if a given number is a power of two
// for example 2^2 = 4
// 4 is a power of 2,  so it returns True

export function isPowerOfTwo(n: number): boolean {
    if (n <= 0){
        return false
    }

    while (n > 1) {
        if (n % 2 !== 0){
            return false
        }
        n = n / 2
    }

    return true
}

