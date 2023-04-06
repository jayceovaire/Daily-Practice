// Count the number of Vowels in a given string and return the number counted

function getCount(str){
    let copy = str.split('')
    let vowels = 0
    for(let i = 0; i < copy.length; i++){
        switch (true){
            case (copy[i] === 'a'):
                vowels += 1
                break

            case (copy[i] === 'e'):
                vowels += 1
                break

            case (copy[i] === 'i'):
                vowels += 1
                break

            case (copy[i] === 'o'):
                vowels += 1
                break

            case (copy[i] === 'u'):
                vowels += 1
                break

            default:
                vowels += 0
                break

        }
    }
    return vowels
}

