export function orderedCount(text: string): [string, number][] {
    let order: string[] = []
    let letterCounter: {[key: string]: number} = {}
    let deconstructedText = text.split('')
    for (let i = 0; i < deconstructedText.length; ++i){
        if (!letterCounter[deconstructedText[i]]){
            letterCounter[deconstructedText[i]] = 1
            order.push(deconstructedText[i])
        }
        else{
            letterCounter[deconstructedText[i]] += 1
        }
    }
    let resultList: [string, number][] = order.map( char => [char, letterCounter[char]])

    return resultList
}

