function listFactory(numFalse: number, numTrue: number): boolean[] {
    const falses = new Array(numFalse).fill(false);
    const trues = new Array(numTrue).fill(true);
    return falses.concat(trues);
}

function two_crystal_balls(breaks: boolean[]): string {
    let jmpAmount = Math.floor(Math.sqrt(breaks.length))

    let i = jmpAmount
    for (; i < breaks.length; i += jmpAmount){
        if (breaks[i]){
            break;
        }
    }
    i -= jmpAmount

    for(let j = -1; j < jmpAmount && i < breaks.length; ++j, ++i){
        if (breaks[i]){
            return `The balls break at floor ${i + 1}`
        }
    }
    return 'Error'
}

// Testing with the factory function
for(let i = 0; i < 100; ++i) {
    const list = listFactory(100 - i - 1, i + 1);
    console.log(two_crystal_balls(list));
}
