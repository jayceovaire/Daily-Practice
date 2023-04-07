// find and return the smallest and largest numbers in a given array

const min = function(list){
    let copy = list.slice()
    return Math.min(...copy)
}

const max = function(list){
    let copy = list.slice()
    return Math.max(...copy)
}