// Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

// The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

// Mind the input validation.

let ar = [1,2,3,4]

function sumArray(array) {
  if (!Array.isArray(array) || array.length <= 1) {
    return 0;
  }
  else{
  let copy = array.slice(0);
  let result = 0;
  copy = copy.map(Number).sort(function(a, b) {
    return a - b;
  });
  copy.pop();
  copy.shift();
  for (let i = 0; i < copy.length; i++) {
    result += copy[i];
    }
    return result;
  }
}

