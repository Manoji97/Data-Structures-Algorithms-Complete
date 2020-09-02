/*

    Find Number of Unique numbers in an SORTED Array  

    Example 1   =>  [1, 1, 1, 1, 4,5,6]   =>  4

    Exapmle 2   =>  [3,4,4,6,6,7]   => 5


    Time Complexity  Provided Solution is O(n)
*/

const CountUniqueNumber = (arr) => {
  if (arr.length === 0) return 0;
  let i = 0;
  for (let j = 1; j < arr.length; j++) {
    if (arr[i] !== arr[j]) {
      i++;
      arr[i] = arr[j];
    }
  }
  return i + 1;
};

let array = [3, 4, 4, 6, 6, 7];
console.log(CountUniqueNumber(array));
