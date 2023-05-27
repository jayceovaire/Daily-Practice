
export function remove(s: string): string {
    let fixedS = s
    if(fixedS.slice(-1) === '!'){
        fixedS = s.slice(0, -1)
    }
    return fixedS
}