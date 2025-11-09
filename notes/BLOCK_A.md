# 🧠 Block A – Foundations & Binary Search Workbook

*(Duration ≈ 2 hours total)*

---

## 1️⃣  What Is an Algorithm?

> An **algorithm** is a finite, step-by-step computational procedure that transforms inputs → desired outputs.

**Properties**

* Definiteness – every step clear
* Finiteness – ends after finite steps
* Input/Output – has at least one input & output
* Effectiveness – every step is doable

**Practice:**   
List 3 daily-life examples of algorithms ⬇️

1. _________ 2. _________ 3. _________

---

## 2️⃣  Asymptotic Analysis
here function is g(n), f(n) is the order of growth, in the worst case its maximum growth rate, in the average its as same as or exact growth rate and in the best its the minimum growth rate...
| Notation                 | Meaning                            | Intuition / Example                   |
| ------------------------ | ---------------------------------- | ------------------------------------- |
| **O(f(n))**              | Upper bound/worst  case            | *≤ c·f(n) for large n* – “worst-case” |
| **Ω(f(n))**              | Lower bound/best case              | *≥ c·f(n)* – “best-case”              |
| **Θ(f(n))**              | Tight bound/average case           | both upper & lower                    |
| **o(f(n))**, **ω(f(n))** | Strictly smaller / strictly larger | rarely used in coding                 |

### Common Growth Orders

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n)
< O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

**Memory trick:** “log–n–nlogn–n²–2ⁿ–n!”

🧩 **Exercise:**
Rank these by growth (fastest → slowest):
`n log n`, `2ⁿ`, `log n`, `n²`, `√n`, `n!`
→ Answer: _________

---

## 3️⃣  Analyzing Loops (Find Complexity)

1. **Single loop**

```cpp
for(int i=0;i<n;i++) {...}
```

→ Runs n times → O(n)

2. **Nested loop**

```cpp
for(i=0;i<n;i++)
  for(j=0;j<n;j++)
```

→ n × n = n² → O(n²)

3. **Logarithmic**

```cpp
for(i=1;i<n;i*=2)
```

→ ⟹ log₂n iterations → O(log n)

---

## 4️⃣  Recurrence Relations

**Definition:** cost = cost of subproblems + cost to combine.

### Common Forms

| Recurrence         | Example Algorithm    | Solution    |
| ------------------ | -----------------    | ----------- |
| T(n)=T(n/2)+O(1)   | Binary Search        | O(log n)    |
| T(n)=2T(n/2)+O(n)  | Merge Sort           | O(n log n)  |
| T(n)=T(n−1)+O(n)   | Insertion Sort       | O(n²)       |
| T(n)=7T(n/2)+O(n²) | Strassen Matrix Mult.| O(n^2.81)   |

### Master Theorem Quick View

For T(n)=a T(n/b)+f(n):

* f(n) smaller → O(n^{log_b a})
* f(n) same → O(n^{log_b a} log n)
* f(n) bigger → O(f(n))

🧩 **Derive by Hand:**

1. T(n)=3 T(n/2)+n² → _________
2. T(n)=2 T(n/2)+n → _________
3. T(n)=T(n/2)+1 → _________

---

## 5️⃣  Binary Search Core Concept

**Idea:**
On a sorted array, repeatedly halve the search interval.

**Steps**

1. Compute mid = (l + r)/2
2. If arr[mid]==x → found
3. If arr[mid] > x → search left
4. Else → search right
5. Repeat until l > r

### Base Code

```cpp
int binarySearch(vector<int>& a,int x){
  int l=0,r=a.size()-1;
  while(l<=r){
    int m=l+(r-l)/2;
    if(a[m]==x) return m;
    else if(a[m]<x) l=m+1;
    else r=m-1;
  }
  return -1;
}
```
### Pseudo code
```cpp
function BINARY_SEARCH(A, N, X)
    low = 0             // Initialize the start of the search range
    high = N - 1        // Initialize the end of the search range

    while low is less than or equal to high do
        mid = floor((low + high) / 2) // Calculate the middle index

        if A[mid] is equal to X then
            return mid  // Target found
        else if A[mid] is less than X then
            low = mid + 1 // Discard the lower half
        else // A[mid] is greater than X
            high = mid - 1 // Discard the upper half
        end if
    end while

    return -1           // Target not found
end function
```



**Time:** O(log n) **Space:** O(1)

🧠 Why log n? → Each step halves the range ⇒ log₂n comparisons.

---

## 6️⃣  Binary Search Variants

| Variant                      | Goal                         | Key Condition                 |
| ---------------------------- | ---------------------------- | ----------------------------- |
| **Lower Bound**              | first index ≥ x              | if (arr[mid] ≥ x) r = mid − 1 |
| **Upper Bound**              | first index > x              | if (arr[mid] > x) r = mid − 1 |
| **First True**               | first true of predicate P(i) | template while(low < high)    |
| **Search in Infinite Array** | find x w/o knowing n         | expand r*=2 until arr[r] ≥ x  |

**Exercise:**
Implement lower_bound manually and test vs STL.
What’s the difference between returning `l` vs `r+1` in your code? → _________

---

## 7️⃣  Edge Cases & Debug Tips

* Overflow: use `mid = l + (r - l) / 2`
* Infinite loop: ensure the bounds change (l++, r--)
* Duplicates: check equality direction carefully
* Empty array: handle n = 0

🧩 **Trace Exercise:**
Given arr = [2, 4, 6, 8, 10], x = 8.
Fill the table:

| Step |  l  |  r  | mid | arr[mid] | Action |
| :--: | :-: | :-: | :-: | :------: | :----: |
|   1  |  0  |  4  |     |          |        |
|   2  |     |     |     |          |        |
|   3  |     |     |     |          |        |

---

## 8️⃣  Complexity Recap

| Operation              | Time     | Space |
| ---------------------- | -------- | ----- |
| Linear Search          | O(n)     | O(1)  |
| Binary Search          | O(log n) | O(1)  |
| Insert in sorted array | O(n)     | O(1)  |
| Delete in array        | O(n)     | O(1)  |

---

## 9️⃣  Quick Test (5 Qs)

1. Difference between Θ and O? → _________
2. Derive T(n)=2T(n/2)+O(1) → _________
3. What is the average #comparisons in Binary Search? → _________
4. Name two real-world uses of Binary Search pattern → _________
5. Why is log n the time complexity of binary search? → _________

---

## 🔁  Reflection & Next Step

> *“I can now compute time complexities from loops and recurrences,
> and code binary search variants confidently.”*

Next Block 👉 **Sorting & Selection (Block B)**
Prepare: revise Master Theorem and recurrence trees once before moving.

---

### 🧩  Optional Mini-Challenge (If You Finish Early)

Write a function `findSqrt(int x)` using binary search (precision to 0.001).
Then note its complexity and why it still works for floats.

---

✅ **Deliverables after completing this workbook**

1. `search/binary_search.cpp` + tested
2. `cheatsheet.md` updated with complexities & recurrences
3. `progress.md` Block A marked ✅
4. Ready to enter **Block B – Sorting & Selection**

---
