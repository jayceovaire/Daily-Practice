
// The main idea is to count all the occurring characters in a string.
// If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
// What if the string is empty? Then the result should be empty object literal, {}.

function count(string){
    if(typeof string === 'string'){

        let result = {}

        for (let i = 0; i < string.length; i++) {
            const char = string[i]
            result[char] = (result[char] || 0) + 1
        }
        return result
    }
    return {}
}

