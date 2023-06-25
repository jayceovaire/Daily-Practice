
// write a function that takes in the number of mangoes you are leaving with and how much you paid for them
// you get 1 free mango for every 2 that you buy.
// example (9, 5) -> 30
// buy 6 at 5 dollars per, get 3 free and pay $30

export function mango(quantity: number, price: number): number {
    let paidMangoes = 0
    let freeMangoes = 0
    let freeCounter = 0
    while (quantity > 0){
        quantity -= 1
        paidMangoes += 1
        freeCounter += 1
        if (freeCounter === 2){
            freeMangoes += 1
            quantity -= 1
            freeCounter = 0
        }

    }
        return (paidMangoes * price)
}

let result = mango(9, 5)
console.log(result) // logs 30