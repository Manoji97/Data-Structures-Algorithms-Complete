/*
This Algorithm Helps in Finding the Shortest Path from one node to another,
 in a graph using Priority Queue.
*/

class SimplePriorityQueue {
  constructor() {
    this.queue = [];
  }

  enqueue(val, priority) {
    const new_value = { val: val, priority };
    this.queue.push(new_value);
    this.sort();
    return true;
  }

  dequeue() {
    return this.queue.shift();
  }

  sort() {
    this.queue.sort((a, b) => a.priority - b.priority);
  }
}

class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
  }
}

class PriorityHeap {
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
        break;
      [this.queue[parentIndex], this.queue[currentIndex]] = [
        this.queue[currentIndex],
        this.queue[parentIndex],
      ];
      currentIndex = parentIndex;
    }
    return this;
  }
  dequeue() {
    const maxPriority = this.queue[0];
    let end = this.queue.pop();
    let length = this.queue.length;
    if (!length) return maxPriority;

    let currentIndex = 0;
    this.queue[currentIndex] = end;
    let leftIndex = 1,
      left,
      rightIndex = 2,
      right,
      current,
      newIndex = currentIndex;

    while (leftIndex < length || rightIndex < length) {
      left = this.queue[leftIndex];
      right = this.queue[rightIndex];
      current = this.queue[currentIndex];
      if (left && left.priority < current.priority) {
        newIndex = leftIndex;
      }
      if (
        right &&
        right.priority < left.priority &&
        right.priority < current.priority
      ) {
        newIndex = rightIndex;
      }
      if (newIndex === currentIndex) break;
      [this.queue[currentIndex], this.queue[newIndex]] = [
        this.queue[newIndex],
        this.queue[currentIndex],
      ];
      currentIndex = newIndex;
      leftIndex = 2 * currentIndex + 1;
      rightIndex = 2 * currentIndex + 2;
    }
    return maxPriority;
  }
}

class Graph {
  constructor() {
    this.AdjacencyList = [];
  }

  addVertex(vertex) {
    if (this.AdjacencyList[vertex]) return false;
    this.AdjacencyList[vertex] = [];
    return true;
  }

  removeVertex(vertex) {
    if (!this.AdjacencyList[vertex]) return fasle;
    this.AdjacencyList[vertex].forEach((neighbour) => {
      this.AdjacencyList[neighbour] = this.AdjacencyList[neighbour].filter(
        (connection) => connection.vertex !== vertex
      );
    });
    delete this.AdjacencyList[vertex];
  }

  addEdge(vertex1, vertex2, weight) {
    if (!(this.AdjacencyList[vertex1] || this.AdjacencyList[vertex2]))
      return false;
    this.AdjacencyList[vertex1].push({ vertex: vertex2, weight });
    this.AdjacencyList[vertex2].push({ vertex: vertex1, weight });
    return true;
  }

  removeEdge(vertex1, vertex2) {
    if (!(this.AdjacencyList[vertex1] || this.AdjacencyList[vertex2]))
      return false;
    this.AdjacencyList[vertex1] = this.AdjacencyList[vertex1].filter(
      (neighbour) => neighbour.vertex !== vertex2
    );
    this.AdjacencyList[vertex2] = this.AdjacencyList[vertex1].filter(
      (neighbour) => neighbour.vertex !== vertex1
    );
    return true;
  }

  dijkstraShorthestPath(startVertex, endVertex) {
    if (!(this.AdjacencyList[startVertex] || this.AdjacencyList[endVertex]))
      return false;
    let PQ = new PriorityHeap();
    let distances = {};
    let previous = {};
    let minVertex,
      newDistance,
      finalPath = [];

    for (const vertex in this.AdjacencyList) {
      if (vertex === startVertex) {
        distances[vertex] = 0;
        PQ.enqueue(vertex, 0);
      } else {
        distances[vertex] = Infinity;
        PQ.enqueue(vertex, Infinity);
      }
      previous[vertex] = null;
    }

    while (PQ.queue.length) {
      minVertex = PQ.dequeue().val;
      if (minVertex === endVertex) {
        //console.log(distances, previous);

        while (previous[minVertex]) {
          finalPath.push(previous[minVertex]);
          minVertex = previous[minVertex];
        }
        finalPath.reverse();
        finalPath.push(endVertex);
        return finalPath;
      }
      this.AdjacencyList[minVertex].forEach((neighbour) => {
        newDistance = distances[minVertex] + neighbour.weight;
        if (newDistance < distances[neighbour.vertex]) {
          distances[neighbour.vertex] = newDistance;
          previous[neighbour.vertex] = minVertex;
          PQ.enqueue(neighbour.vertex, newDistance);
        }
      });
    }
    return false;
  }
}

let G = new Graph();

G.addVertex("A");
G.addVertex("B");
G.addVertex("C");
G.addVertex("D");
G.addVertex("E");
G.addVertex("F");

G.addEdge("A", "B", 4);
G.addEdge("A", "C", 2);
G.addEdge("B", "E", 3);
G.addEdge("C", "D", 2);
G.addEdge("C", "F", 4);
G.addEdge("D", "E", 3);
G.addEdge("D", "F", 1);
G.addEdge("F", "E", 1);

/*

    A    -4-    B
    2               3
    C  -2-  D  -3-   E 
        4    1    1 
              F  
*/
