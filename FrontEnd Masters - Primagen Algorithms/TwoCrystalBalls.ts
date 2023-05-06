// Given two crystal balls that will break if dropped from high enough
// distance, determine the exact spot in which it will break in the most
// optimized way.

const floors: boolean[] = [false, false, false, false, false, false, false,
    false, false, false, false, false, false, false, false, false, true, true,
    true, true, true, true, true, true, true]


function two_crystal_balls(breaks: boolean[]): string {
    let jmpAmount = Math.ceil(Math.sqrt(breaks.length))


    let i = jmpAmount
    for (; i < breaks.length; i += jmpAmount){
        if (breaks[i]){
            break;
        }
    }
    i -= jmpAmount

    for(let j = 0; j < jmpAmount && i < breaks.length; ++j, ++i){
        if (breaks[i]){
            return `The balls break at floor ${i + 1}`
        }
    }
    return 'Error'
}

// Walk up floors by sqrt of # of floors until ball breaks
// then walk back by sqrt of # of floors and walk back up one floor at a time
// up to where the ball first broke to find earliest breaking point.

console.log(two_crystal_balls(floors))