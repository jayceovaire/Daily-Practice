export function cubeChecker(volume: number, side: number): boolean {
    if (volume === 0 || side === 0){
        return false
    }
    return volume === (side **3)
    
}