
// bubble sort starts at 0th position, checks value of location next to current location, if
// that value is larger than next value, swap locations.

let example: number[] = [7,6,5,4,3,2,1]

function bubbleSort(array: number[]){

  for (let i = 0; i < array.length; ++i){
  for (let j = 0; j < array.length -1 -i; ++j){
    if (array[j] > array[j + 1]){
      const tmp = array[j];
      array[j] = array[j + 1];
      array[j + 1] = tmp;
    }
  }}
}

bubbleSort(example)
console.log(example)

