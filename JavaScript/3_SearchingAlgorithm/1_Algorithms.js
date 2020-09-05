// Searches One by One Element and time Complexity is => O(n)
const LinearSearch = (arr, elem) => {
  for (let i = 0; i < arr.length; i++) {
    if (elem === arr[i]) return i;
  }
  return -1;
};

//console.log(LinearSearch([2, 3, 5, 63, 3, 6, 7, 8], 633));

// (Only on Sorted Array) Searches on Log Scale Element and time Complexity is => O(n)
const BinarySearch = (arr, elem) => {
  if (elem < arr[0] || elem > arr[arr.length - 1]) return -1; //Since its an Sorted Array this can reduce time.
  let left = 0;
  let right = arr.length - 1;
  let middle = Math.floor((left + right) / 2);
  while (arr[middle] !== elem) {
    console.log(left, middle, right);
    if (left >= right) return -1;
    if (arr[middle] < elem) left = middle + 1;
    if (arr[middle] > elem) right = middle - 1;
    middle = Math.floor((left + right) / 2);
  }
  return middle;
};

//console.log(BinarySearch([1, 2, 3, 4, 5, 55, 56, 71, 75], 55));

//Basic SubString Search O(n^2)
const NaiveStringSearch = (longString, shortstring) => {
  let count = 0;
  for (let i = 0; i < longString.length; i++) {
    for (let j = 0; j < shortstring.length; j++) {
      console.log(shortstring[j], longString[i + j]);
      if (shortstring[j] !== longString[i + j]) break;
      if (j === shortstring.length - 1) count++;
    }
  }
  return count;
};

console.log(NaiveStringSearch("i feel so so Good", "so"));
