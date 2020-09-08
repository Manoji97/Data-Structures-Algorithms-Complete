/*

Two Way of Implementing the Graphs are using,
    => AdjacencyList   
    => AdjacentMatrix

    here we are gonna use Adjacency List
*/

class Graph {
  constructor() {
    this.AdjacencyList = {};
  }

  addVertex(vertex) {
    if (this.AdjacencyList[vertex]) return false;
    this.AdjacencyList[vertex] = [];
    return true;
  }

  removeVertex(vertex) {
    if (!this.AdjacencyList[vertex]) return false;
    this.AdjacencyList[vertex].forEach((connection) => {
      this.AdjacencyList[connection] = this.AdjacencyList[connection].filter(
        (connect_vertex) => vertex !== connect_vertex
      );
    });
    delete this.AdjacencyList[vertex];
    return true;
  }

  addEdge(vertex1, vertex2) {
    if (!(this.AdjacencyList[vertex1] || this.AdjacencyList[vertex2]))
      return false;
    this.AdjacencyList[vertex1].push(vertex2);
    this.AdjacencyList[vertex2].push(vertex1);
    return true;
  }

  removeEdge(vertex1, vertex2) {
    if (!(this.AdjacencyList[vertex1] || this.AdjacencyList[vertex2]))
      return false;
    this.AdjacencyList[vertex1] = this.AdjacencyList[vertex1].filter(
      (vertex) => vertex !== vertex2
    );
    this.AdjacencyList[vertex2] = this.AdjacencyList[vertex2].filter(
      (vertex) => vertex !== vertex1
    );
    return true;
  }

  depthFirstResursive(startVertex) {
    let result = [];
    let visited = {};

    let connections;

    const depthFirst = (start_vertex) => {
      connections = this.AdjacencyList[start_vertex];

      visited[start_vertex] = true;
      result.push(start_vertex);
      connections.forEach((vertex) => {
        if (!visited[vertex]) {
          depthFirst(vertex);
        }
      });
    };
    depthFirst(startVertex);

    return result;
  }

  depthfirstIterative(startVertex) {
    let result = [];
    let visited = {};
    let stack = [];
    stack.push(startVertex);
    visited[startVertex] = true;
    let vertex;

    while (stack.length) {
      vertex = stack.pop();

      result.push(vertex);
      this.AdjacencyList[vertex].forEach((connectionVertex) => {
        if (!visited[connectionVertex]) {
          stack.push(connectionVertex);
          visited[connectionVertex] = true; //visited should be marked once pushed to stack , or else it will append multiple times
        }
      });
    }

    return result;
  }

  breadthFirstIterative(startVertex) {
    let result = [];
    let visited = {};
    let queue = [];
    queue.push(startVertex);
    visited[startVertex] = true;
    let vertex;

    while (queue.length) {
      vertex = queue.shift();

      result.push(vertex);
      this.AdjacencyList[vertex].forEach((connectionVertex) => {
        if (!visited[connectionVertex]) {
          queue.push(connectionVertex);
          visited[connectionVertex] = true;
        }
      });
    }

    return result;
  }
}

let G = new Graph();
G.addVertex("A");
G.addVertex("B");
G.addVertex("C");
G.addVertex("D");
G.addVertex("E");
G.addVertex("F");

G.addEdge("A", "B");
G.addEdge("A", "C");
G.addEdge("B", "D");
G.addEdge("D", "E");
G.addEdge("D", "F");
G.addEdge("C", "E");
G.addEdge("E", "F");

/*
        A
    B       c
    D   -   E
        F


*/
