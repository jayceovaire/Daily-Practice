export function greet(name: string, owner: string): string{
    if(name ===  owner){
        return `Hello ${name}`
    }
    return `Hello guest`

}