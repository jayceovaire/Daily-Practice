
// given a starting position and a roll return the new position as pos + roll * 2

export function move(pos: number, roll: number): number {
    let newPosition: number = pos + (roll * 2)
    return newPosition
}
