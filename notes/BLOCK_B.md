# ⚙️ Block B — Sorting & Selection Workbook

*(Duration ≈ 2½ hours)*

---

## 🎯 Learning Goals

| Concept              | Skill Outcome                                                        |
| -------------------- | -------------------------------------------------------------------- |
| Comparison sorting   | Derive Θ(n log n) bounds, know why faster general sort is impossible |
| Implementations      | Code and trace Merge Sort, Quick Sort, Heap Sort                     |
| Non-comparison sorts | Know where Counting/Radix apply                                      |
| Selection            | Implement Quickselect and analyze its expected O(n) behavior         |

---

## 1️⃣  Why Sorting Matters

Sorting is a **primitive for optimization** — once data is ordered, searching, merging, and greedy algorithms become trivial.

### Real-world uses

* Organizing data for binary search or merging logs
* Reducing complexity in geometry or greedy scheduling problems
* Found in library routines: `std::sort`, `Collections.sort`, `Arrays.sort`

---

## 2️⃣  Sorting Landscape

| Algorithm                          | Best       | Average    | Worst      | Stable        | In-place |
| ---------------------------------- | ---------- | ---------- | ---------- | ------------- | -------- |
| **Bubble / Insertion / Selection** | O(n)       | O(n²)      | O(n²)      | Yes / No / No | Yes      |
| **Merge Sort**                     | O(n log n) | O(n log n) | O(n log n) | ✅             | ❌        |
| **Quick Sort**                     | O(n log n) | O(n log n) | O(n²)      | ❌             | ✅        |
| **Heap Sort**                      | O(n log n) | O(n log n) | O(n log n) | ❌             | ✅        |
| **Counting / Radix / Bucket**      | O(n + k)   | O(n + k)   | O(n + k)   | ✅             | ❌        |

---

## 3️⃣  Merge Sort – Divide & Conquer

### Idea

1. Divide array in halves
2. Recursively sort both halves
3. Merge them in linear time

**Recurrence:** T(n)=2 T(n/2)+Θ(n) → Θ(n log n)

**Code**

```cpp
void merge(vector<int>& a,int l,int m,int r){
  vector<int> L(a.begin()+l,a.begin()+m+1),
              R(a.begin()+m+1,a.begin()+r+1);
  int i=0,j=0,k=l;
  while(i<L.size() && j<R.size()) a[k++]= (L[i]<=R[j]?L[i++]:R[j++]);
  while(i<L.size()) a[k++]=L[i++];
  while(j<R.size()) a[k++]=R[j++];
}

void mergeSort(vector<int>& a,int l,int r){
  if(l>=r) return;
  int m=l+(r-l)/2;
  mergeSort(a,l,m);
  mergeSort(a,m+1,r);
  merge(a,l,m,r);
}
```

🧠 Stable but needs O(n) extra space.

🧩 Exercise: Count inversions using merge sort — modify merge step to count when L[i] > R[j].

---

## 4️⃣  Quick Sort – Partition & Recur

### Idea

1. Pick a **pivot**
2. Partition array so left < pivot < right
3. Recursively sort subarrays

**Recurrence:** T(n)=T(k)+T(n−k−1)+Θ(n)

### Code

```cpp
int partition(vector<int>& a,int low,int high){
  int pivot=a[high],i=low-1;
  for(int j=low;j<high;j++)
    if(a[j]<=pivot) swap(a[++i],a[j]);
  swap(a[i+1],a[high]);
  return i+1;
}
void quickSort(vector<int>& a,int low,int high){
  if(low<high){
    int pi=partition(a,low,high);
    quickSort(a,low,pi-1);
    quickSort(a,pi+1,high);
  }
}
```

🧠 Average Θ(n log n) ; Worst Θ(n²) (for sorted input if pivot = last).
💡 Fix: choose pivot randomly ⇒ expected O(n log n).

**Exercise:** Trace quicksort on `[5,2,7,3,9]` and record pivot positions.

---

## 5️⃣  Heap Sort – Tree Selection

### Steps

1. Build max-heap O(n)
2. Repeatedly extract max & heapify O(log n)

```cpp
void heapify(vector<int>& a,int n,int i){
  int largest=i,l=2*i+1,r=2*i+2;
  if(l<n && a[l]>a[largest]) largest=l;
  if(r<n && a[r]>a[largest]) largest=r;
  if(largest!=i){ swap(a[i],a[largest]); heapify(a,n,largest); }
}
void heapSort(vector<int>& a){
  int n=a.size();
  for(int i=n/2-1;i>=0;i--) heapify(a,n,i);
  for(int i=n-1;i>0;i--){ swap(a[0],a[i]); heapify(a,i,0); }
}
```

✅ In-place; ❌ not stable.

**Complexity:** Build O(n)+n log n = O(n log n).

---

## 6️⃣  Counting / Radix Sort (Linear Sorts)

Used when keys are integers in small range [0, k].

**Counting Sort**

```cpp
void countingSort(vector<int>& a,int k){
  vector<int> cnt(k+1),out(a.size());
  for(int x:a) cnt[x]++;
  for(int i=1;i<=k;i++) cnt[i]+=cnt[i-1];
  for(int i=a.size()-1;i>=0;i--){
    out[cnt[a[i]]-1]=a[i];
    cnt[a[i]]--;
  }
  a=out;
}
```

**Time:** O(n + k) ; Stable.

**Radix Sort:** Apply counting sort on each digit (LSD→MSD) ⇒ O(d (n + k))

---

## 7️⃣  Quickselect – Selection Algorithm

Find k-th smallest element using Quick Sort’s partition logic.

```cpp
int quickSelect(vector<int>& a,int l,int r,int k){
  if(l==r) return a[l];
  int pi=partition(a,l,r);
  int len=pi-l+1;
  if(k==len) return a[pi];
  else if(k<len) return quickSelect(a,l,pi-1,k);
  else return quickSelect(a,pi+1,r,k-len);
}
```

**Expected Time:** O(n) (using random pivot).
Used in **median-of-medians** for deterministic O(n).

🧩 Practice: Find k-th smallest & k-th largest in random array of 100 ints.

---

## 8️⃣  Complexity Derivations (Write Out)

| Algorithm     | Recurrence      | Result         | Notes            |
| ------------- | --------------- | -------------- | ---------------- |
| Merge Sort    | 2T(n/2)+n       | Θ(n log n)     | D&C              |
| Quick Sort    | T(k)+T(n−k−1)+n | Θ(n log n) avg | Randomized pivot |
| Heap Sort     | n log n         | Θ(n log n)     | In-place         |
| Counting Sort | n + k           | Θ(n + k)       | Non-comparison   |
| Quickselect   | T(n/2)+Θ(n)     | Θ(n) avg       | Selection        |

---

## 9️⃣  Compare & Choose

| Situation                | Recommended      |
| ------------------------ | ---------------- |
| Large data, recursion ok | Merge Sort       |
| Average case, in-place   | Quick Sort       |
| Memory limited           | Heap Sort        |
| Integers in small range  | Counting / Radix |
| Find median              | Quickselect      |

---

## 🔁  Reflection & Cheatsheet Update

**Update `cheatsheet.md` sections:**

```
### Sorting & Selection Key Points
- Comparison-based lower bound: Ω(n log n)
- Merge Sort: stable, Θ(n log n), O(n) space
- Quick Sort: in-place, avg Θ(n log n), worst Θ(n²)
- Heap Sort: in-place, Θ(n log n)
- Counting/ Radix: linear if key range k = O(n)
- Quickselect: expected O(n)
```

---

## 📈  Add to `progress.md`

```
## Block B — Sorting & Selection
- [x] Merge Sort implemented + inversion count test ✅
- [x] Quick Sort implemented (random pivot) ✅
- [x] Heap Sort implemented ✅
- [x] Counting Sort tested ✅
- [x] Quickselect coded ✅
- [ ] Radix Sort pending
Takeaway: mastered divide-and-conquer and comparison vs non-comparison sorts.
```

---

## 🧠  Quick Self-Check

1. Why can’t any comparison-based sort beat O(n log n)?
2. What property makes Merge Sort stable but Heap Sort not?
3. When does Quick Sort hit worst case? How to avoid it?
4. Why can Counting Sort be O(n)? What’s its limitation?
5. Derive recurrence of Quick Sort for average case.

---

✅ **Deliverables after Block B**

* `sorting/` folder with 5+ implementations
* Updated `cheatsheet.md` and `progress.md`
* Small test inputs in `tests/`
* Ready for **Block C: Divide & Conquer Advanced**

---
