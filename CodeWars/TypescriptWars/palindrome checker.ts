export function isPalindrome(x: string): boolean {
    return x.toLowerCase() === x.toLowerCase().split('').reverse().join('')
}

