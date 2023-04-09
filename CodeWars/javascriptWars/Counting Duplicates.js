// write a function that will return the count of distinct case-insensitive characters
// and numeric digits that occur more than once in the input string.

const test = ['aa']
const test2 = ['aabb']
const test3 = ['ab11']

function duplicateCount(text){
    let copy = text
    let count = 0
    const charCounts = new Map()
    for(let i = 0; i < copy.length; i++){
        const char = copy[i].toLowerCase()
        const charCount = charCounts.get(char) || 0
        charCounts.set(char, charCount + 1)
        if(charCount === 1){
            count++
        }
    }
    return count

}

function duplicateCount2(text) {
  let charCounts = {};
  let count = 0;

  for (let i = 0; i < text.length; i++) {
    let char = text.charAt(i).toLowerCase();
    if (charCounts[char]) {
      if (charCounts[char] === 1) {
        count++;
      }
      charCounts[char]++;
    } else {
      charCounts[char] = 1;
    }
  }

  return count;
}


duplicateCount(test)
duplicateCount(test2)
duplicateCount(test3)