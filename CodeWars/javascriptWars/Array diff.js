// Your goal in this kata is to implement a difference function,
// which subtracts one list from another and returns the result.
// It should remove all values from list a, which are present in
// list b keeping their order.



function arrayDiff(a, b) {
    return a.filter(item => !b.includes(item) )
}


function arrayDiff2(a, b){
    let result = []
    for(let i = 0; i < a.length; i++){
        if(!b.includes(a[i])){
            result.push(a[i])
        }
    }
    return result
}

