# DAA Cheatsheet — 1-page quick reference

## 1. Big-O / Notation
O(...) = worst-case, Θ(...) = tight bound, Ω(...) = best-case.
Common growth: O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)

## 2. Master Theorem (quick)
T(n) = a T(n/b) + f(n)
- If f(n) = O(n^{log_b a - ε}) -> T(n)=Θ(n^{log_b a})
- If f(n) = Θ(n^{log_b a}) -> T(n)=Θ(n^{log_b a} log n)
- If f(n) = Ω(n^{log_b a + ε}) and regularity -> T(n)=Θ(f(n))

## 3. Common recurrences
- T(n)=2T(n/2)+Θ(n) -> Θ(n log n)
- T(n)=T(n-1)+Θ(1) -> Θ(n)
- T(n)=aT(n/b)+Θ(1) -> Θ(n^{log_b a})

## 4. Sorting summary (quick table)
Algorithm | Best | Avg | Worst | Space | Stable | In-place
---|---:|---:|---:|---:|---:|---
Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No
Quick (rand) | O(n log n) | O(n log n) | O(n^2) | O(log n) | No | Yes
Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes
Counting/Radix | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes/No | No

## 5. DP patterns (how to spot)
- Overlapping subproblems + optimal substructure -> DP
- Steps: define state, recurrence, base, compute order, reconstruct (if needed)
- Common templates: 1D array DP, 2D DP, bitmask DP, tree DP

## 6. Graphs (cheat)
- BFS/DFS: O(V+E)
- Dijkstra (PQ): O(E log V) ; requires non-negative weights
- Bellman-Ford: O(VE) ; detects negative cycles
- Kruskal (with DSU): O(E log E)

## 7. Greedy checks
- Are local greedy choices provably safe? (exchange argument / matroid)
- Counterexample quick-check: test small cases where greedy might fail (example: coin set {1,3,4} for 'greedy coin change').

## 8. Quick code & test commands
- Compile C++: `g++ -std=gnu++17 file.cpp -O2 -o file`
- Run: `./file < input.txt`
- Run all tests: `bash tests/run_all.sh`

## 9. Debugging checklist (recursion)
- Print parameters at entry and exit
- Check base case coverage
- Small input brute force vs output compare

## 10. Quick mental map
- If problem asks shortest path + non-negative weights -> Dijkstra
- If asked for optimal subset with weights -> try DP (knapsack style)
- If asked to schedule/choose intervals -> greedy (sort by finishing time)
