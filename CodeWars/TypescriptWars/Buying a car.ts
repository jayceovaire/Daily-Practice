export function nbMonths(startPriceOld: number, startPriceNew: number, savingperMonth: number, percentLossByMonth: number): number[]{
    let savings = 0
    let currentCar = startPriceOld
    let newCar = startPriceNew
    let secondMonth = false
    let percentLoss = percentLossByMonth
    let months = 0
    while ((savings + currentCar) < newCar){
        if (secondMonth){
            percentLoss += 0.5
        }

        currentCar *= (100 - percentLoss) / 100
        newCar *= (100 - percentLoss) / 100
        savings += savingperMonth
        months ++
        secondMonth = !secondMonth

    }

    return [months, Math.round(savings + currentCar - newCar)]
}



