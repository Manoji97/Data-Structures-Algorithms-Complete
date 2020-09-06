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

  breadthFirstSearch() {
    let queue = [];
    let visited = [];
    queue.push(this.root);
    while (queue.length > 0) {
      let node = queue.shift();
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
      visited.push(node.val);
    }
    return visited;
  }

  depthFirstPreOrderSearch() {
    let output = [];
    const traverse = (node) => {
      output.push(node.val);
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
    };
    traverse(this.root);
    return output;
  }

  depthFirstPostOrderSearch() {
    let output = [];
    const traverse = (node) => {
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
      output.push(node.val);
    };
    traverse(this.root);
    return output;
  }

  depthFirstInOrderSearch() {
    let output = [];
    const traverse = (node) => {
      if (node.left) traverse(node.left);
      output.push(node.val);
      if (node.right) traverse(node.right);
    };
    traverse(this.root);
    return output;
  }
}

let BST = new BinarySearchTree();
BST.insert(10);
BST.insert(4);
BST.insert(6);
BST.insert(12);
BST.insert(20);
BST.insert(18);
BST.insert(11);
BST.insert(2);
BST.insert(1);

/*
                10
          4             12
      2      6     11            20
    1                       18



for the given tree BreadthFirst Search OutPut Must be => [10,4,12,2,6,11,20,1,18]
    will provide all the nodes in breath first order

for the given tree DepthFirst PreOrder Search OutPut Must be => [10,4,2,1,6,12,11,20,18]
    will provide the order in Root => Left => Right (Recursively) for each node

for the given tree DepthFirst PostOrder Search OutPut Must be => [1,2,6,4,18,11,20,12,10]
    will provide the order in Left => Right => Root (Recursively) for each node

for the given tree DepthFirst InOrder Search OutPut Must be => [1,2,4,6,10,11,12,18,20]
    will provide the order in Left => Root => Right (Recursively) for each node 
    this will result to a Sorted Array.


BreadthFirst Search takes more Space than any Depth First Search ,
But Time Complexity is same since , both visit all nodes.
*/
