// Works Well for Online realtime data joining the array

// time complexity is O(n^2)

//refer net for concept

//Maintains the Sort Order on the Left Side.

//Fixes the 1st element as sorted and starts from 2nd element
//checks if 2nd element is smaller that previos element and id smaller swaps
//then moves to 3rd , if 3rd element is smaller tah 2nd  store that 3rd(curreny value) in a variable
//then change 3rd to 2nd value and if 2nd is smaller than current value assign 1st to 2nd and
//finally once u find teh correct  spot assign the current value to that index(spot).

const InsertionSort = (arr) => {
  let currentVal;
  for (let i = 1; i < arr.length; i++) {
    currentVal = arr[i];
    for (let j = i - 1; j <= 0; j--) {
      if (arr[j] < currentVal) break;
      arr[j + 1] = arr[j];
    }
    arr[j + 1] = arr[currentVal];
  }
  return arr;
};

console.log(InsertionSort([7, 2, 5, 8, 4, 1, 10, 45, 34, 78, 3, 5, 56, 6]));
