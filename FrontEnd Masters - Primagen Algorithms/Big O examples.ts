let teststring = 'test me'
function sum_char_codes(n: string): number {
    let sum = 0;
    for(let i = 0; i < n.length; i++){
        sum += n.charCodeAt(i);

        // If charcodeAt(i) is E return current sum
        if (n.charCodeAt(i) === 69){
            return sum;
        }
    }
    return sum;
}

console.log(sum_char_codes(teststring))


// O(1)
// O(n)
// O(n^2)
// O(log n^2)
// O(log n)
// O(n^3)
// O(n^4)
