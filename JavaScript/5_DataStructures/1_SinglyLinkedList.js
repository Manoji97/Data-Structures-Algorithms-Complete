class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SingleLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  printAll() {
    // Just For Seeing , not Efficient
    if (!this.head) return -1;
    let node = this.head;
    let output = [];
    while (node) {
      output.push(node.val);
      node = node.next;
    }
    return output;
  }
  push(val) {
    //Append new val to the end of the list
    const new_node = new Node(val);
    if (!this.head) {
      this.head = new_node;
      this.tail = new_node;
    } else {
      this.tail.next = new_node;
      this.tail = new_node;
    }
    this.length++;
    return true;
  }
  pop() {
    //pop the last value of the list
    if (!this.head) return false;
    if (this.length === 1) {
      let node = this.head;
      this.head = null;
      this.tail = null;
      this.length = 0;
      return node.val;
    }
    let node = this.head;
    let previousNode = node;
    while (node !== this.tail) {
      previousNode = node;
      node = node.next;
    }
    previousNode.next = null;
    this.tail = previousNode;
    this.length--;
    return node.val;
  }

  shift(val) {
    //add new element to the Starting of the list
    const new_node = new Node(val);
    if (!this.head) this.push(val);
    else {
      let oldHead = this.head;
      new_node.next = oldHead;
      this.head = new_node;
      this.length++;
      return true;
    }
  }

  unShift() {
    //Removes the 1st element from the list
    if (this.length < 1) this.pop();
    else {
      this.head = this.head.next;
      this.length--;
      return true;
    }
  }

  get(index) {
    //Get the Node at Index "index"
    if (index < 0 || index >= this.length) return false;
    let node = this.head;
    for (let i = 1; i <= index; i++) {
      node = node.next;
    }
    return node;
  }

  set(val, index) {
    let setNode = this.get(index);
    if (!oldNode) {
      return false;
    }
    setNode.val = val;
    return true;
  }

  insert(val, index) {
    const new_node = new Node(val);
    let connectNode = this.get(index - 1);
    if (!connectNode) {
      return false;
    }
    let toConnectNode = connectNode.next;
    connectNode.next = new_node;
    new_node.next = toConnectNode;
    return true;
  }

  remove(index) {
    let connectNode = this.get(index - 1);
    if (!connectNode) {
      return false;
    }
    connectNode.next = connectNode.next.next;
    return true;
  }
  reverse() {}
}

let l = new SingleLinkedList();
l.push(52);
l.push(63);
l.push(78);
l.push(49);
l.push(5);
