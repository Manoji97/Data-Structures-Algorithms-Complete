// Frequency Counter is used for comparing the frequency of each element in array 1 to array 2

/*
    Example 1  =>  [1, 2, 4] ,  [1, 4, 16]  => true
    Example 2  =>  [2, 3, 4],   [4, 9, 5]   => false
*/

// Time Complexity for this solution is O(n)

const FrequencyCounter = (arr1, arr2) => {
  let arr1Obj = {};
  let arr2Obj = {};
  if (arr1.length !== arr2.length) {
    return false;
  }
  for (const val of arr1) {
    arr1Obj[val] = ++arr1Obj[val] || 1;
  }
  for (const val of arr2) {
    arr2Obj[val] = ++arr2Obj[val] || 1;
  }
  for (const key in arr1Obj) {
    if (!arr2Obj.hasOwnProperty(key)) {
      return false;
    }
    if (arr2Obj[key] !== arr1Obj[key]) {
      return false;
    }
  }
  return true;
};

let a = [1, 2, 3, 5];
let b = [5, 1, 3, 2];
console.log(FrequencyCounter(a, b));
