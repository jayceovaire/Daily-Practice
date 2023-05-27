
// Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total.
// Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
// Write a code that gives out the total amount for different days(d).

export function rentalCarCost(d: number): number {
    let cost = d * 40
    if (d >= 7){
        cost = cost - 50
    }
    else if (d >= 3){
        cost = cost - 20
    }

    return cost
}