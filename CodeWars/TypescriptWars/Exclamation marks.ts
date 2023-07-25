export function remove(s: string): string {
    let result = ''
    for (let i = 0; i < s.length; i++){
        if (s[i] !== '!'){
            result += s[i]
        }
    }
    result += '!'


    return result
}