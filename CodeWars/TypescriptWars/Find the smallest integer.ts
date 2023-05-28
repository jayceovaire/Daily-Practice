
// write a function that returns the smallest number in a list of numbers

export function findSmallestInt(args: number[]): number {
    let smallest = args[0]
    for (let i = 1; i < args.length; i++){
        if(args[i] < smallest){
            smallest = args[i]
        }
    }
    return smallest
}

export function findSmallestInt2(args: number[]): number {
    return Math.min(...args)
}