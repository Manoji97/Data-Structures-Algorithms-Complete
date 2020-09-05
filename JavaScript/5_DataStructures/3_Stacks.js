class SimpleStack {
  //Not Efficent with large Stacks
  constructor() {
    this.stack = [];
  }
  push(val) {
    this.stack.push(val);
    return this.stack.length;
  }
  pop() {
    return this.stack.pop();
  }
}

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  printAll() {
    let stack = [];
    if (!this.first) return null;
    let node = this.first;
    while (node) {
      stack.push(node.val);
      node = node.next;
    }
    return stack;
  }

  push(val) {
    const new_node = new Node(val);
    if (!this.first) {
      this.first = new_node;
      this.last = new_node;
    } else {
      new_node.next = this.first;
      this.first = new_node;
    }
    return ++this.size;
  }

  pop() {
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
