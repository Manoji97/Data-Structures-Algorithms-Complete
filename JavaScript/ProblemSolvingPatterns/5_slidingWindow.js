/*
    input array and a number
    Find Maximum Sum of (number) consecutive numbers in that Array  

    Example 1   =>  [1, 1, 1, 1, 4,5,6], 4   =>  17

    Exapmle 2   =>  [7,4,4,6,6,7], 3   => 19


*/

const NaiveMethod = (arr, num) => {
  if (num > arr.length) return null;
  let maxSum = -Infinity;
  let tempSum = 0;
  for (let i = 0; i <= array.length - num; i++) {
    for (let j = i; j < num + i; j++) {
      tempSum += arr[j];
    }
    maxSum = Math.max(maxSum, tempSum);
    tempSum = 0;
  }
  return maxSum;
};

const SlidingWindow = (arr, num) => {
  let maxSum = 0;
  let tempSum = 0;
  for (let i = 0; i < num; i++) {
    maxSum += arr[i];
  }
  tempSum = maxSum;

  for (let i = num; i < arr.length; i++) {
    tempSum = tempSum - arr[i - num] + arr[i];
    maxSum = Math.max(maxSum, tempSum);
  }
  return maxSum;
};

const array = [7, 4, 4, 6, 6, 7];
const num = 3;
console.log(NaiveMethod(array, num));
console.log(SlidingWindow(array, num));
