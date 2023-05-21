

export function getRealFloor(n: number): number {

    if (n > 13) {
        return n - 2
    }
    else if (n <= 0)
        return n
    else {
        return n - 1
    }
}