
// bubble sort starts at 0th position, checks value of location next to current location, if
// that value is larger than next value, swap locations.

let example: number[] = [1, 3, 7, 4, 2]

function bubbleSort(array: number[]): void {
  for (let i = 0; i < array.length; i++) {
    for (let j = 1; j < array.length - i; j++) {
      if (array[j] < array[j - 1]) {
        const tmp = array[j];
        array[j] = array[j - 1];
        array[j - 1] = tmp;
      }
    }
  }
}

bubbleSort(example)
console.log(example)