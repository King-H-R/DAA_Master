# 🕸️ Block 6 – Graphs: Traversal & Shortest Paths

*(Duration ≈ 2.5 hours total)*

---

## 1️⃣ Graph Basics – Quick Refresher

A **graph G(V,E)** has:

* **Vertices (V):** nodes / points.
* **Edges (E):** connections (directed or undirected).

### Representations

| Representation   | Structure           | Space    | When to use                 |
| ---------------- | ------------------- | -------- | --------------------------- |
| Adjacency Matrix | 2-D array [V][V]    | O(V²)    | Dense graphs                |
| Adjacency List   | vector<vector<int>> | O(V + E) | Sparse graphs – most common |

---

## 2️⃣ BFS – Breadth-First Search (Traversal & Shortest Path in Unweighted Graphs)

### Intuition

Think of ripples spreading out from a source node — BFS explores **level by level**.

### Algorithm (Queue based)

```cpp
void bfs(int start, vector<vector<int>>& adj, int V){
    vector<bool> vis(V,false);
    queue<int> q;
    vis[start]=true;
    q.push(start);

    while(!q.empty()){
        int u=q.front(); q.pop();
        cout<<u<<" ";
        for(int v: adj[u])
            if(!vis[v]){
                vis[v]=true;
                q.push(v);
            }
    }
}
```

### Properties

* Time O(V + E)
* Space O(V)
* Finds shortest path (fewest edges) in **unweighted** graphs.
* Works for both directed & undirected graphs.

### Use Cases

* Level order traversal, shortest route in unweighted maps, connectivity checking.

🧩 **Exercise**: Write BFS that returns `dist[v]` = distance from source for all v.

---

## 3️⃣ DFS – Depth-First Search

### Intuition

Go as **deep** as possible along each branch before backtracking — like exploring a maze.

### Recursive Version

```cpp
void dfsUtil(int u, vector<vector<int>>& adj, vector<bool>& vis){
    vis[u]=true;
    cout<<u<<" ";
    for(int v: adj[u])
        if(!vis[v]) dfsUtil(v,adj,vis);
}
void dfs(int V, vector<vector<int>>& adj){
    vector<bool> vis(V,false);
    for(int i=0;i<V;i++)
        if(!vis[i]) dfsUtil(i,adj,vis);
}
```

### Properties

* Time O(V + E)
* Space O(V) (stack + recursion)
* Reveals connected components.
* Order of discovery gives **topological**, **cycle**, and **connectivity** info.

### DFS Applications

* Topological sort
* Detect cycles
* Strongly connected components (Kosaraju)
* Path existence

🧩 **Exercise**: Modify DFS to return discovery & finish time of each vertex.

---

## 4️⃣ Topological Sorting (for DAGs)

### Definition

A **topological order** of a DAG (Directed Acyclic Graph) is a linear ordering of vertices such that

> if (u → v) ∈ E, then u appears before v in the order.

### Two Methods

#### 1. DFS Post-Order

Push vertex to stack after visiting all neighbors → reverse stack for order.

```cpp
void topoDFS(int u, vector<vector<int>>& adj, vector<bool>& vis, stack<int>& st){
    vis[u]=true;
    for(int v:adj[u])
        if(!vis[v]) topoDFS(v,adj,vis,st);
    st.push(u);
}
vector<int> topoSort(int V, vector<vector<int>>& adj){
    vector<bool> vis(V,false); stack<int> st;
    for(int i=0;i<V;i++) if(!vis[i]) topoDFS(i,adj,vis,st);
    vector<int> order;
    while(!st.empty()){ order.push_back(st.top()); st.pop(); }
    return order;
}
```

#### 2. Kahn’s Algorithm (BFS + Indegree)

Compute indegree of each vertex; push all indegree 0 vertices to queue;
pop → append to order → reduce neighbors’ indegrees.

**Complexity:** O(V + E)

🧠 Use for scheduling, build systems, prerequisite problems (e.g., course order).

---

## 5️⃣ Dijkstra’s Algorithm – SSSP for Non-Negative Weights

### Intuition

Expands outward greedily like BFS, but chooses the vertex with smallest tentative distance.
Requires a **priority queue (min-heap)** for efficiency.

### Code (Simplified)

```cpp
vector<int> dijkstra(int V, vector<vector<pair<int,int>>>& adj, int src){
    vector<int> dist(V, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    dist[src]=0;
    pq.push({0,src});

    while(!pq.empty()){
        auto [d,u]=pq.top(); pq.pop();
        if(d!=dist[u]) continue; // outdated entry
        for(auto [v,w]: adj[u]){
            if(dist[v] > dist[u]+w){
                dist[v] = dist[u]+w;
                pq.push({dist[v],v});
            }
        }
    }
    return dist;
}
```

### Properties

* Works only if **all weights ≥ 0**.
* Time O((V + E) log V) using priority queue.
* Greedy + Relaxation idea.

### Key Concept: Relaxation

> Relax(u,v,w): if dist[v] > dist[u]+w → update dist[v].

🧠 Visualization: Think of growing a set of finalized shortest distances (SPT = Shortest Path Tree).

🧩 **Exercise:** Modify to also store `parent[]` and reconstruct the shortest path.

---

## 6️⃣ Bellman-Ford Algorithm – Handles Negative Edges

### Idea

Repeatedly relax all edges V−1 times.
If any edge can still be relaxed on Vth iteration → negative cycle exists.

### Code

```cpp
bool bellmanFord(int V, vector<tuple<int,int,int>>& edges, int src, vector<int>& dist){
    dist.assign(V, INT_MAX);
    dist[src]=0;
    for(int i=1;i<V;i++){
        for(auto [u,v,w]: edges)
            if(dist[u]!=INT_MAX && dist[v]>dist[u]+w)
                dist[v]=dist[u]+w;
    }
    // check for negative cycle
    for(auto [u,v,w]: edges)
        if(dist[u]!=INT_MAX && dist[v]>dist[u]+w)
            return false; // negative cycle found
    return true;
}
```

### Complexity

* Time O(V × E)
* Works with negative weights.
* Detects negative cycles 🚫.

### Use Cases

* Currency arbitrage, graphs with credit/debt values.

🧩 **Exercise:** Create a graph with a negative cycle and verify detection.

---

## 7️⃣ Comparative Summary

| Algorithm        | Works with Neg Edges | Detect Neg Cycle | Time Complexity | Technique            |
| ---------------- | -------------------- | ---------------- | --------------- | -------------------- |
| **BFS**          | No (weights = 1)     | No               | O(V + E)        | Level Traversal      |
| **DFS**          | –                    | –                | O(V + E)        | Recursion (depth)    |
| **Dijkstra**     | ❌                    | ❌             | O(E log V)      | Greedy + PQ          |
| **Bellman-Ford** | ✅                    | ✅             | O(VE)           | Iterative Relaxation |

---

## 8️⃣ Cheatsheet Updates

Add this section to `cheatsheet.md`:

```
### Graph Algorithms Quick Ref
BFS → O(V+E), queue, shortest path (unweighted)  
DFS → O(V+E), stack/recursion, components & cycle detection  
Topological Sort → O(V+E), DAG only  
Dijkstra → O(E log V), non-negative weights, PQ based  
Bellman-Ford → O(VE), negative weights ok, cycle detect  
Relaxation: if dist[v] > dist[u]+w → update  
```

---

## 9️⃣ Progress Log Template for `progress.md`

```
## Block 6 – Graphs Traversal & SSSP
- [x] BFS implemented and tested ✅  
- [x] DFS implemented ✅  
- [x] Topological Sort (Kahn + DFS) ✅  
- [x] Dijkstra (PQ version) ✅  
- [x] Bellman-Ford tested with negative cycle ✅  
Takeaway: understood traversal patterns + relaxation concept for weighted graphs.
```

---

## 🔁 Mini Self-Test (5 Qs)

1. Why does Dijkstra fail with negative weights?
2. What’s the main difference between BFS and Dijkstra?
3. How many iterations does Bellman-Ford need to detect a negative cycle?
4. Why is topological sort only for DAGs?
5. In Dijkstra, when can you stop the algorithm early?

---

✅ **Deliverables after Block 6**

* `graphs/bfs_dfs.cpp`
* `graphs/topo.cpp`
* `graphs/dijkstra.cpp`
* `graphs/bellman_ford.cpp`
* Updated `cheatsheet.md` and `progress.md`

---
