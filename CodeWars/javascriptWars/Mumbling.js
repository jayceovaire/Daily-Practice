
//accum("abcd") -> "A-Bb-Ccc-Dddd"
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
// accum("cwAt") -> "C-Ww-Aaa-Tttt"

function accum(s){
    let copy = s.split('')
    let result = []
    for(let i = 0; i < copy.length; i++){
        if(i > 0) {
            result.push('-')
        }
        result.push(copy[i].toUpperCase())
        let counter = i
        while(counter > 0){
            result.push(copy[i].toLowerCase())
            counter -= 1
        }
    }
    return result.join('')
}

let test = accum('abcd')
console.log(test)
//__________________________________>Second Solve<______________________________________________________________



function accum2(s) {
  return s.split('')
    .map((char, index) => {
      return char.toUpperCase() + char.toLowerCase().repeat(index);
    })
    .join('-');
}

let test2 = accum2('abcd');
console.log(test2); // outputs "A-Bb-Ccc-Dddd"

//__________________________________>Recursive Solve<______________________________________________________________

function accum3(s, i = 0, result = []) {
  if (i >= s.length) {
    return result.join('-');
  }
  const char = s.charAt(i).toUpperCase() + s.charAt(i).toLowerCase().repeat(i);
  result.push(char);
  return accum(s, i + 1, result);
}

let test3 = accum3('abcd');
console.log(test3); // outputs "A-Bb-Ccc-Dddd"






