class MaxBinayHeap {
  constructor() {
    this.values = [];
  }

  insert(val) {
    /*
    Time Complexity => O(log n)
this function helps to insert new value into heap.
once you insert it to the end of array , it will find its parents and check if its parent value is more
, if its more it breaks or swaps with parent => this happens Recursively.
*/
    this.values.push(val);
    let currentIndex = this.values.length - 1;
    let parentIndex;
    while (currentIndex > 0) {
      parentIndex = Math.floor((currentIndex - 1) / 2);
      if (this.values[parentIndex] >= this.values[currentIndex]) break;
      [this.values[parentIndex], this.values[currentIndex]] = [
        this.values[currentIndex],
        this.values[parentIndex],
      ];
      currentIndex = parentIndex;
    }
    return this;
  }

  extractMax() {
    /*
this Function helps in reteriving the Max value present in the heap in O(1).
here we return value at [0] position since its always MAX and swap the last value to root
and recursively find its childrens and swap if the children are greater than the root.
*/
    let maxValue = this.values[0];
    let parent = this.values.pop();
    let length = this.values.length;
    if (length === 0) return maxValue;

    //Bubble Down
    let parentIndex = 0;
    this.values[parentIndex] = parent;
    let left,
      leftIndex = 1,
      right,
      rightIndex = 2;

    let newIndex = parentIndex;

    while (leftIndex < length || rightIndex < length) {
      left = this.values[leftIndex];
      right = this.values[rightIndex];
      parent = this.values[parentIndex];

      if (left && left > parent) {
        newIndex = leftIndex;
      }
      if (right && right > left && right > parent) {
        newIndex = rightIndex;
      }
      if (newIndex === parentIndex) break;

      [this.values[parentIndex], this.values[newIndex]] = [
        this.values[newIndex],
        this.values[parentIndex],
      ];
      parentIndex = newIndex;
      leftIndex = 2 * parentIndex + 1;
      rightIndex = 2 * parentIndex + 2;
    }
    return maxValue;
  }
}

let BH = new MaxBinayHeap();

/*
Binary Heap is a special trea where only the Maximum value will be as root in
 Max Binary Heap and Minimum in Min Binary Heap.




*/
