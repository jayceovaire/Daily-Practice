export function predictAge(age1: number, age2: number, age3: number, age4: number, age5: number, age6: number, age7: number, age8: number): number {
    
    let sumList: number[] = [age1, age2, age3, age4, age5, age6, age7, age8]
    let summedNums: number = 0
    for (let i = 0; i < sumList.length; i++){
        let currentNum: number = sumList[i]**2
        summedNums += currentNum
    }
    console.log(Math.floor(Math.sqrt(summedNums)/ 2))
    return Math.floor(Math.sqrt(summedNums) / 2)
    
}

export function predictAge2(...ages: number[]){
    return Math.floor(Math.sqrt(ages.reduce((acc, num) => acc += num**2, 0))/ 2)
}


console.log(predictAge2(1,2,3,4,5,6,7,8))
