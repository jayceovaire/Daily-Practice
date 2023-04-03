// Return the number of the century for the Input year

function century(year){
    if(year <= 0){
        return 0
    }
    else if(year <= 100){
        return 1
    }
    else{
        return 1 + century(year - 100)
    }
}



