//Basic Bubble Sorting Time Complexity => O(n^2)
//No Optimaization Technique invloved

const BasicBubbleSort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // syntax for swapping in JS
      }
    }
  }
  return arr;
};

//console.log(BasicBubbleSort([7, 2, 5, 8, 4, 1, 10, 45, 34, 78, 3, 5, 56, 6]));

//Basic Bubble Sorting Time Complexity => O(n^2) little less becaus eeach time we reduce teh iteration count
// because each cycle the biggest number is moved to last , so no use in comparing the last element again

const BubbleSort_Optimized_1 = (arr) => {
  for (let i = arr.length; i >= 0; i--) {
    for (let j = 0; j < i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // syntax for swapping in JS
      }
    }
  }
  return arr;
};

//console.log(BubbleSort_Optimized_1([7, 2, 5, 8, 4, 1, 10, 45, 34, 78, 3, 5, 56, 6]));

//Second Optimized Version of Bubble Sort, in this case time complexity is O(n^2)
//sometimes it can be O(n) if teh array is already almost Sorted.
// in this method we break out if no Swapping happened in that particular iteration.

const BubbleSort_Optimized_2 = (arr) => {
  let noSwap = true;
  for (let i = arr.length; i >= 0; i--) {
    for (let j = 0; j < i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        noSwap = false;
      }
    }
    if (noSwap) break;
  }
  return arr;
};

console.log(
  BubbleSort_Optimized_2([7, 2, 5, 8, 4, 1, 10, 45, 34, 78, 3, 5, 56, 6])
);
