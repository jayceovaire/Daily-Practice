
// This program tests the life of an evaporator containing a gas.
// We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day
// (evap_per_day) and the threshold (threshold) in percentage beyond which the evaporator is no longer useful.
// All numbers are strictly positive.
// The program reports the nth day (as an integer) on which the evaporator will be out of use.

export function evaporator(content: number, evapPerDay: number, threshold: number): number {
    let mlContent = content
    let thresholdPoint = content * (threshold / 100)
    let evapPercent = evapPerDay / 100
    let days = 0
    while(mlContent > thresholdPoint){
       mlContent = mlContent - (mlContent * evapPercent)
        days += 1
    }


    return days
}
