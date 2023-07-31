export function warnTheSheep(queue: string[]): string {
    const wolfIndex = queue.indexOf('wolf')

    if(wolfIndex === queue.length - 1) {
        return 'Pls go away and stop eating my sheep'
    }
    else{
        const sheepPosition = queue.length - wolfIndex - 1
        return `Oi! Sheep number ${sheepPosition}! You are about to be eaten by a wolf!`
    }

}

let testCase = ["sheep", "sheep", "wolf", "sheep", "sheep", "sheep", "sheep"]

console.log(warnTheSheep(testCase))