/*

Time Complexity => O(kn)  k => maxdigits and n => number of elems in array
Space Complexity => O(n+k)

Radix Sort is a fun Sorting Algorithm

Uses the digits to sort the array

for base 10 numbers(decimals) we have 10 buckets from (0 to 9)

we find max number of digits from the whole given array

we loop from 0 to max digits as i variable
    and classify the elems in num array into 10 buckets based on their number on i th digit
    and concat every array from 10 buckets (preserve the order)
    then again do the same process until you reach max digits

*/

const GetDigit_at_i = (num, i) => {
  return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
};

const GetDigits_of_Num = (num) => {
  if (num === 0) return 0;
  return Math.floor(Math.log10(num)) + 1;
};

const GetMax_Digits = (arr) => {
  let maxDigits = 0;
  for (let i = 0; i < arr.length; i++) {
    maxDigits = Math.max(GetDigits_of_Num(arr[i]), maxDigits);
  }
  return maxDigits;
};

const RadixSort = (arr) => {
  const maxDigits = GetMax_Digits(arr);
  for (let i = 0; i < maxDigits; i++) {
    //Create 10 buckets i.e arrays
    let digitBuckets = Array.from({ length: 10 }, () => []);
    for (let j = 0; j < arr.length; j++) {
      digitBuckets[GetDigit_at_i(arr[j], i)].push(arr[j]);
    }
    arr = [].concat(...digitBuckets);
  }
  return arr;
};

console.log(RadixSort([3445, 45, 3456, 45687, 35, 3, 2, 2, 78]));
