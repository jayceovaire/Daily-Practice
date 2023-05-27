
// write a function that accepts a name and returns how many lightsabers that person owns.
// only Zach owns lightsabers, 18 to be precise.

export function howManyLightsabersDoYouOwn(name?: any): number {
    if (name != 'Zach'){
        return 0
    }
    return 18
}