// create a function that takes a list of non-negative integers and
// strings and returns a new list with the strings filtered out.


function filter_list(list) {
 let result = list.filter(item => typeof item === 'number')
    return result
}

