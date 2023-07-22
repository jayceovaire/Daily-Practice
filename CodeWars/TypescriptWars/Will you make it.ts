
// Given a distance to travel as well as the mpg economy of a car and the fuel left in the tank
// write a function that returns True if you can make it to your destination with the current fuelLeft


export const zeroFuel = (distance: number, mpg: number, fuelLeft: number): boolean => {
    return distance <= (mpg * fuelLeft)
}

