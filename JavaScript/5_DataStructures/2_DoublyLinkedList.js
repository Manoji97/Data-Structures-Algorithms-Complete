class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  printAll() {
    let output = [];
    if (!this.head) return false;
    let node = this.head;
    while (node) {
      output.push(node.val);
      node = node.next;
    }
    return output;
  }

  push(val) {
    const new_node = new Node(val);
    if (!this.head) {
      this.head = new_node;
      this.tail = new_node;
    } else {
      this.tail.next = new_node;
      new_node.prev = this.tail;
      this.tail = new_node;
    }
    this.length++;
    return true;
  }

  pop() {
    if (!this.head) return false;
    let oldTail = this.tail;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
      this.length = 0;
      return oldTail;
    }
    this.tail = oldTail.prev;
    this.tail.next = null;
    oldTail.prev = null;
    this.length--;
    return oldTail;
  }

  shift(val) {
    const new_node = new Node(val);
    if (!this.head) {
      this.head = new_node;
      this.tail = new_node;
    } else {
      this.head.prev = new_node;
      new_node.next = this.head;
      this.head = new_node;
    }
    this.length++;
    return true;
  }

  unShift() {
    if (!this.head) return false;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
      this.length = 0;
      return;
    }
    let oldHead = this.head;
    this.head = this.head.next;
    this.head.prev = null;
    oldHead.next = null;
    this.length--;
    return oldHead;
  }

  get(index) {
    if (index < 0 || index >= this.length) return false;
    let node;
    if (index <= this.length / 2) {
      node = this.head;
      for (let i = 1; i <= index; i++) {
        node = node.next;
      }
    } else {
      node = this.tail;
      for (let i = this.length - 2; i >= index; i--) {
        node = node.prev;
      }
    }
    return node;
  }

  set(val, index) {
    let setNode = this.get(index);
    if (!setNode) {
      return false;
    }
    setNode.val = val;
    return true;
  }

  insert(val, index) {
    if (index < 0 || index > this.length) return false;
    if (index === 0) return this.shift(val);
    if (index === this.length) return this.push(val);
    const new_node = new Node(val);
    let prevNode = this.get(index - 1);
    new_node.next = prevNode.next;
    prevNode.next.prev = new_node;
    prevNode.next = new_node;
    new_node.prev = prevNode;
    this.length++;
    return true;
  }

  remove(index) {
    if (index < 0 || index >= this.length) return false;
    if (index === 0) return this.unShift();
    if (index === this.length - 1) return !!this.pop();
    let removeNode = this.get(index);
    removeNode.prev.next = removeNode.next;
    removeNode.next.prev = removeNode.prev;
    removeNode.next = null;
    removeNode.prev = null;
    this.length--;
    return true;
  }

  reverse() {
    if (!this.head) return false;
    let node = this.head;
    this.head = this.tail;
    this.tail = node;
    for (let i = 0; i < this.length; i++) {
      let next_node = node.next;
      [node.next, node.prev] = [node.prev, node.next];
      node = next_node;
    }
    return true;
  }
}

let d = new DoublyLinkedList();
