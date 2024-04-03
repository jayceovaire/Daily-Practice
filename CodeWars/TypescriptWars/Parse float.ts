type MaybeNumber = number | null

export function parseF(s: string): MaybeNumber {

    const num = Number.parseFloat(s)
    return isNaN(num) ? null : num

    }

