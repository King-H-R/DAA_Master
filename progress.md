# Progress Log — DAA Sprint
Start: YYYY-MM-DD HH:MM (Asia/Kolkata)
Language: C++ / Python

## Legend
[ ] -> not started
[x] -> done
[P] -> partial / in progress

---

## 00 Setup
- [x] repo created, cheatsheet.md added
- [x] tests/run_all.sh template added

---

## 01 Foundations & Binary Search
- [x] Asymptotics notes added to cheatsheet (time: 40m)
- [x] Binary search variants implemented: `sorting/binary_search.cpp`
  - Tests: passed 10 random cases (stable) ✅
  - Complexity: O(log n)
  - Notes: Remember off-by-one with upper_bound

---

## 02 Sorting
- [x] Merge Sort (`sorting/merge.cpp`)
  - Tests: random arrays up to n=1e5, inversion count verified vs brute O(n^2) for n<=100
  - Complexity: Θ(n log n), Space: O(n)
  - Takeaway: implement stable merge carefully (use temp vector)
- [x] Quick Sort (`sorting/quick.cpp`)
  - Tests: randomized pivot avoids worst-case on sorted input
  - Complexity: avg Θ(n log n), worst Θ(n^2)
  - Bug noted: stack overflow on degenerate recursion -> fixed by tail recursion elimination/pivot randomization
- [ ] Heap Sort (`sorting/heap.cpp`)
  - Tests: ---
  - Notes: build-heap O(n)
- [ ] Counting/Radix
  - Notes: only for integers/range bounded inputs

---

## 03 Divide & Conquer
- [x] Inversion count (`dnq/inversions.cpp`)
  - Tests: validated
- [P] Closest Pair (`dnq/closest_pair.cpp`)
  - Notes: implement divide step; tested sample only

---

## 04 Greedy & MST
- [x] Activity selection (`greedy/activity.cpp`)
- [x] Huffman (`greedy/huffman.cpp`)
- [x] Kruskal + DSU (`graphs/kruskal.cpp`)
  - Tests: small graph passed
- [ ] Prim

---

## 05 Dynamic Programming
- [x] Fibonacci memo/tab
- [x] 0/1 Knapsack (`dp/knapsack.cpp`)
  - Tests: small W verified vs brute
- [x] LCS (`dp/lcs.cpp`) ✔
- [x] Edit Distance (`dp/edit_distance.cpp`) ✔
- [x] LIS O(n log n) (`dp/lis.cpp`) ✔
- [ ] Matrix Chain Multiplication

---

## 06 Graphs traversal & SSSP
- [x] BFS/DFS (`graphs/bfs_dfs.cpp`) ✔
- [x] Topological sort (`graphs/topo.cpp`) ✔
- [x] Dijkstra (`graphs/dijkstra.cpp`) — tested on grid, PQ version ✔
- [x] Bellman-Ford (`graphs/bellman_ford.cpp`) — negative cycle detection ✔

---

## 07 Backtracking & Strings
- [x] N-Queens (`backtracking/nqueens.cpp`) ✔
- [x] KMP prefix function (`strings/kmp.cpp`) ✔
- [ ] Z-algorithm

---

## 08 Flow & Matching
- [P] Edmonds-Karp (`graphs/edmonds_karp.cpp`) - partial
- [ ] Hopcroft-Karp

---

## Self-test & Final
- Mini-exam (date/time): [PASS/FAIL]: PASS
- Problems solved: sorting(✓), greedy(✓), dp(✓), graph(✓), backtracking(✓)
- Next actions: implement remaining algorithms, add unit tests for edge cases
