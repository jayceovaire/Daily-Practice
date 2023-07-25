export function points(games: string[]): number {
    let s = games.join('').split('')
    let siftedScores = ''
    let xScore = 0
    for (let i = 0; i < s.length; i++){
        if(s[i] !== ':'){
            siftedScores += s[i]
        }
    }
    for(let i = 0; i < siftedScores.length; i+=2){
        let j = i + 1
        if(siftedScores[i] > siftedScores[j]){
            xScore += 3
        }
        if (siftedScores[i] === siftedScores[j]){
            xScore += 1
        }
    }
    return xScore
}

export function points2(games: string[]): number {
    let total = 0
    for (let game of games){
        if(game[0] > game[2]){
            total += 3
        }
        else if (game[0] === game[2]){
            total += 1
        }
    }
    return total
}

console.log(points(["1:0","2:0","3:0","4:0","2:1","1:3","1:4","2:3","2:4","3:4"]))