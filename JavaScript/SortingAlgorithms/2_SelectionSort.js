//this is Same as Bubble Sort instead we bring minimum to on end and the time Complexity is O(n^2)
// the one advantage for this Algo is can reduce no of Swaps

//unlike BubbleSort this doesnt do intermidiate Swap , it Just selects the minimum and swap to the particular index

//Each time Finds the Lowest value from the Remaining Array and puts it in the desired index
//so that the worst case time complexity is also O(n^2)

const SelectionSort = (arr) => {
  let lowest;
  for (let i = 0; i < arr.length; i++) {
    lowest = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[lowest]) {
        lowest = j;
      }
    }
    if (i !== lowest) {
      // this line is Responsible for Reducing the Number of Swaps
      [arr[i], arr[lowest]] = [arr[lowest], arr[i]];
    }
  }
  return arr;
};

console.log(SelectionSort([7, 2, 5, 8, 4, 1, 10, 45, 34, 78, 3, 5, 56, 6]));
