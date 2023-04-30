// given a number between 0 and 9 return the number as a word


function switchItUp(num){

    switch (num){
        case 0:
            return 'Zero'
            break;

        case 1:
            return 'One'
            break;
        case 2:
            return 'Two'
            break;

        case 3:
            return 'Three'
            break;

        case 4:
            return 'Four'
            break;

        case 5:
            return 'Five'
            break;

        case 6:
            return 'Six'
            break;

        case 7:
            return 'Seven'
            break;

        case 8:
            return 'Eight'
            break;

        case 9:
            return 'Nine'
            break;

        default:
            return 'None'
            break;
    }

}

function switchItUp2(num){
    const words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return words[num]
}