export function number(array: string[]): string[]{

   let result: string[] = array.map((line, index) => `${index + 1}: ${line}`)

    return result
}

