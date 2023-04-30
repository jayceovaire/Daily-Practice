
// Big O of Linear Search - O(n)

const haystack: number [] = [1,2,3,4,5,6,7,8,9,10]
const needle: number = 8

function linearSearch(haystack: number[], needle: number): any{
    for (let i = 0; i < haystack.length; i++){
        if (haystack[i] === needle){
            return true + 'needle found at location [' + haystack[i] + ']';
        }
    }
    return false;
}

console.log(linearSearch(haystack, needle))