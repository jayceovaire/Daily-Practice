

export function mouthSize(animal: string): string {

    if(animal !== 'alligator' && animal !== 'ALLIGATOR'){
        return 'wide'
    }
    return 'small'
}

export const mouthSize2 = (animal: string): string => /alligator/i.test(animal) ? 'small' : 'wide'
