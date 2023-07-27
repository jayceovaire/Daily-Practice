export const towerBuilder = (nFloors: number): string[] => {
    let tower: string[] = [];
    for (let i = 0; i < nFloors; i++) {
        let spaces = ' '.repeat(nFloors - i - 1);
        let stars = '*'.repeat(2 * i + 1);
        let floor = spaces + stars + spaces;
        tower.push(floor);
    }
    return tower;
}


console.log(towerBuilder(10))
