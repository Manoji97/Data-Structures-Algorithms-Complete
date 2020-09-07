class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
  }
}

class PriorityQueue {
  constructor() {
    this.queue = [];
  }

  enqueue(val, priority) {
    const new_node = new Node(val, priority);
    this.queue.push(new_node);

    let currentIndex = this.queue.length - 1;
    let parentIndex;

    while (currentIndex > 0) {
      parentIndex = Math.floor((currentIndex - 1) / 2);
      if (this.queue[parentIndex].priority < this.queue[currentIndex].priority)
        return this;
      [this.queue[parentIndex], this.queue[currentIndex]] = [
        this.queue[currentIndex],
        this.queue[parentIndex],
      ];
      currentIndex = parentIndex;
    }
    return this;
  }

  dequeue() {
    let maxPriority = this.queue[0];
    let parent = this.queue.pop();
    let length = this.queue.length;
    if (length === 0) return maxPriority;
    let parentIndex = 0;
    this.queue[parentIndex] = parent;

    let left,
      leftIndex = 1,
      right,
      rightIndex = 2;
    let newIndex = parentIndex;
    while (leftIndex < length || rightIndex < length) {
      left = this.queue[leftIndex];
      right = this.queue[rightIndex];
      parent = this.queue[parentIndex];

      if (left && left.priority < parent.priority) {
        newIndex = leftIndex;
      }
      if (
        right &&
        right.priority < left.priority &&
        right.priority < parent.priority
      ) {
        newIndex = rightIndex;
      }

      if (newIndex === parentIndex) break;
      [this.queue[newIndex], this.queue[parentIndex]] = [
        this.queue[parentIndex],
        this.queue[newIndex],
      ];
      parentIndex = newIndex;

      leftIndex = 2 * parentIndex + 1;
      rightIndex = 2 * parentIndex + 2;
    }
    return maxPriority;
  }
}

let PQ = new PriorityQueue();

/*
Priority Queue is same like Binary Heap.

but its Minimum Binary Heap with respect priority => 1 = high priority, 5 = less priority

Time Complexity => O(1) getting
                => O(log n) enqueing 
*/
