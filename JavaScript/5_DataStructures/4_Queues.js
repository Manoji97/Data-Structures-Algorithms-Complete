class SimpleQueue {
  constructor() {
    this.queue = [];
  }
  enqueue(val) {
    this.queue.push(val);
  }
  dequeue() {
    this.queue.shift();
  }
}

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  printAll() {
    let queue = [];
    if (!this.first) return null;
    let node = this.first;
    while (node) {
      queue.push(node.val);
      node = node.next;
    }
    return queue;
  }

  enqueue(val) {
    const new_node = new Node(val);
    if (!this.first) {
      this.first = new_node;
      this.last = new_node;
    } else {
      this.last.next = new_node;
      this.last = new_node;
    }
    return ++this.size;
  }

  dequeue() {
    if (!this.first) return -1;
    let oldFirst = this.first;
    if (this.size === 1) {
      this.first = null;
      this.last = null;
      this.size = 0;
    } else {
      this.first = this.first.next;
      this.size--;
    }
    oldFirst.next = null;
    return oldFirst;
  }
}
