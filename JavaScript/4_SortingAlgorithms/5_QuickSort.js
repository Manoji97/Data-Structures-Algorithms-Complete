/*

Time Complexity => O(n log(n)) worst case O(n^2) if all teh pivots choosed are minimum
Space Complexity => O(log n)

uses Divide and conquer

start with the 1st number and bring all the numbers that are smll to its left side and large numners to uts right side
repeat the same process for left recursively and right recursively


===> Pivot function to return the crct location (pivot) of the given array
    =>  take 1st element
    =>  loop through next and swap all teh small numbers to left 
    =>  count the number of small numbers
    =>  return the count


===> QuickSort Pseudo Code
    =>  Use Recursion to split the Array with the pivot u got on previous recursion
    =>  Base condition is if left index is less than right teh code should work else return array
    =>  do swap for left part and right part recursively

*/

const Pivot = (arr, start = 0, end = arr.length) => {
  let ind = start;
  let currentVal = arr[start];
  for (let i = ind + 1; i < end; i++) {
    // i = ind +1 can reduce the number of loops
    if (currentVal > arr[i]) {
      ind++;
      [arr[ind], arr[i]] = [arr[i], arr[ind]];
    }
  }
  [arr[start], arr[ind]] = [arr[ind], arr[start]];
  return ind;
};

console.log(Pivot([5, 10, 1, 6, 2, 2, 3])); // Output => 4

const QuickSort = (arr, left = 0, right = arr.length - 1) => {
  if (left < right) {
    let pivotIndex = Pivot(arr, left, right);
    //recursions
    QuickSort(arr, left, pivotIndex - 1);
    QuickSort(arr, pivotIndex + 1, right);
  }

  return arr;
};

console.log(QuickSort([5, 10, 1, 6, 2, 2, 3]));

//[5, 10, 1, 6, 2, 2, 3]

/*



*/
