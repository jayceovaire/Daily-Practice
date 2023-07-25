export class G964 {
    public static nbDig(n: number, d: number): number {
        let exponentList: number[] = []
        for (let i = 0; i <= n; i++){
            let currentNum = i**2
            exponentList.push(currentNum)
        }
        let counter = 0
        let newExponentList = exponentList.join('').split((''))
        for (let i = 0; i < newExponentList.length; i++){
            if(Number(newExponentList[i]) === d){
                counter ++
            }
        }
        return counter
    }
}



G964.nbDig(10,1)