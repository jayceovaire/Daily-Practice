// Check to see if a string has the same amount of Xs and Os.
// The method must return a boolean and be case-insensitive.
// The string can contain any char.

function XO(str) {
    let copy = str.slice()
    let numX = 0
    let numO = 0
    for(let i = 0; i < copy.length; i++){
        if(copy[i].toLowerCase() === 'x'){
            numX += 1
        }
        else if(copy[i].toLowerCase() === 'o'){
            numO += 1
        }
    }
    if(numX === numO){
        return true
    }
    else{
        return false
    }
}

console.log(XO("afa")) //expect true X = 0 O = 0
console.log(XO('xo')) //expect true X = O
console.log(XO('xoxx')) //expect false X != O
console.log(XO('123')) //expect true X = 0 O = 0





