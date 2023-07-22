export const nbYear = (p0: number, percent: number, aug: number, p: number): number => {
    let years = 0;
    let current_population = p0;
    while (current_population < p) {
        current_population = current_population * (1 + percent / 100) + aug;
        current_population = Math.floor(current_population)
        years++;
    }
    return years;
}

