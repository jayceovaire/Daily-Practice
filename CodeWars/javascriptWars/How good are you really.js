
function betterThanAverage(classPoints, yourPoints) {
    const totalScore = classPoints.reduce((accumulator, iterator) => accumulator + iterator, 0);
    const average = (totalScore + yourPoints) / (classPoints.length + 1);
    return yourPoints > average;
}

function betterThanAverage(classPoints, yourPoints) {
    let totalScore = 0;
    for (let i = 0; i < classPoints.length; i++) {
        totalScore += classPoints[i];
    }
    let average = (totalScore + yourPoints) / (classPoints.length + 1);

    return yourPoints > average
}


