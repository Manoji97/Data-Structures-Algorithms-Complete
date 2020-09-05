/*

Time Complexity => O(n log(n))
Space Complexity => O(n)

uses Divide and conquer

Assumes that an Array with 0 or 1 element is always sorted, so we split up teh array into smaller pieces


===> Merge 2 Arrays Pseudo Code
    =>  create empty result array
    =>  while we didnt check the min(arr1.len, arr2.len) out of both arrray er loop and push it to result
    =>  push the remaining elements to result if anything left


===> MergeSort Pseudo Code
    =>  Use Recursion to split the Array to make it have only one element
    =>  Base condition is if array len is 1 return arr
    =>  then merge left and right recursively

*/

const Merge2_Arrays = (arr1, arr2) => {
  const result = [];
  let i = 0;
  let j = 0;
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else {
      result.push(arr2[j]);
      j++;
    }
  }
  while (i < arr1.length) {
    result.push(arr1[i]);
    i++;
  }
  while (j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }
  return result;
};

const MergeSort = (arr) => {
  //Base Condition
  if (arr.length <= 1) return arr;
  let middle = Math.floor(arr.length / 2);
  let left = MergeSort(arr.slice(0, middle));
  let right = MergeSort(arr.slice(middle));
  return Merge2_Arrays(left, right);
};

console.log(MergeSort([2, 6, 3, 0, 7, 56, 32, 5]));

/*



                            [10,24,73,76]
                            mergeSort([10,24,76,73])
        [10, 24]                   merge                [73,76]                         
        mergeSort([10,24])                               mergeSort([76,73])
[10]      merge     [24]                        [76]        merge       [73]
mergeSort([10])     mergeSort([24])             mergeSort([76])         mergeSort([73])


*/

/*

Reason for n Log(n)


==> 1st reason for log n is 
        decomposition if 8 elements , the array divides 3 times which is lograthemic relation
==> 2nd , reason for n is
        the Merge2Array function needs to perform n number of comparisions 

thats why on total its O(n log(n))
*/
