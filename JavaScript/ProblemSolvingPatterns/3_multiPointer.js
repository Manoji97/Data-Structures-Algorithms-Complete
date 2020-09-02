/*

Find 1st 2 elements in an SORTED array which will return 0 on addition.

    Example 1   =>  [-3,-2,-1,0,1,2,3]   =>  [-3,3]

    Exapmle 2   =>  [-4,-2,0,1,7]   => undefined


    Time Complexity for the naive method is O(n^2), and For Best Provided Solution is O(n)
*/

const NaiveMethod = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (arr[i] + arr[j] === 0) {
        return [arr[i], arr[j]];
      }
    }
  }
};

const MultiPointer = (arr) => {
  let left = 0;
  let right = arr.length - 1;
  while (left < right) {
    let sum = arr[left] + arr[right];
    if (sum === 0) {
      return [arr[left], arr[right]];
    } else if (sum < 0) {
      left++;
    } else {
      right--;
    }
  }
};

let array = [-5, -4, -2, -1, 0, 1, 2, 3];

console.log(NaiveMethod(array));
console.log(MultiPointer(array));
