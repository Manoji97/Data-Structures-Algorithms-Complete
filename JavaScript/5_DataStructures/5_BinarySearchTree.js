class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
    this.totalNodes = 0;
  }

  insert(val) {
    const new_node = new Node(val);
    if (!this.root) {
      this.totalNodes++;
      this.root = new_node;
      return this;
    }
    let node = this.root;
    while (true) {
      if (val === node.val) return false;
      if (val < node.val) {
        if (node.left === null) {
          node.left = new_node;
          this.totalNodes++;
          return this;
        }
        node = node.left;
      } else if (val > node.val) {
        if (node.right === null) {
          node.right = new_node;
          this.totalNodes++;
          return this;
        }
        node = node.right;
      }
    }
  }

  find(val) {
    if (!this.root) return false;
    let node = this.root;
    while (node) {
      if (val < node.val) {
        node = node.left;
      } else if (val > node.val) {
        node = node.right;
      } else {
        return node;
      }
    }
    return false;
  }
}

let BST = new BinarySearchTree();
