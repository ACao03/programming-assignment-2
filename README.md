# Cache Eviction Policy Comparison

Student: Anthony Cao  
UFID: 22929899  

---

## How to Run


python src/cache.py data/file1.in   
python src/cache.py data/file2.in   
python src/cache.py data/file3.in


---

## Input Format


k m     
r1 r2 r3 ... rm


Where:

- `k` = cache capacity  
- `m` = number of requests  
- `r1 ... rm` = sequence of integer requests

---

## Output Format


FIFO : <misses>     
LRU : <misses>  
OPTFF : <misses>


---

## Example


python src/cache.py tests/example.in

Input:  
3 12    
1 2 3 4 1 2 5 1 2 3 4 5

Output:     
FIFO  : 9   
LRU   : 10      
OPTFF : 7   

---

# Question 1: Empirical Comparison

| Input File | k | m | FIFO | LRU | OPTFF |
|------------|---|---|------|------|-------|
| File1 | 3 | 50 | 38 | 42 | 26 |
| File2 | 4 | 60 | 51 | 49 | 28 |
| File3 | 5 | 75 | 57 | 66 | 31 |

### Observations

OPTFF consistently produces the fewest cache misses. This is expected because OPTFF has knowledge of the future request sequence and can evict the item whose next use is farthest away.

FIFO and LRU perform somewhat similarly, though their results vary depending on the request pattern. In these experiments, FIFO and LRU sometimes perform close to each other, but LRU can still perform worse if recently used items are not requested again soon.

---

# Question 2: Bad Sequence for LRU

For k = 3, there exists a request sequence where OPTFF incurs strictly fewer misses than LRU.

Example request sequence:


1 2 3 4 1 2 5 1 2 3 4 5


### Miss Counts

| Policy | Misses |
|------|------|
| LRU | 10 |
| OPTFF | 7 |

### Explanation

LRU evicts the least recently used item without knowing future requests. In this sequence, LRU sometimes removes items that will soon be requested again.

OPTFF examines the future request sequence and evicts the item whose next use occurs farthest in the future. Because of this, OPTFF avoids unnecessary evictions and produces fewer cache misses.

This demonstrates that LRU is not always optimal.

---

# Question 3: Proof that OPTFF is Optimal

Proof OPTFF (Beladt's Farthest-in-Future algorithm) is optimal using an exchange argument.  

Let OPT be the OPTFF algorithm and A be any other offline algorithm that knows the entire request sequence. 

Suppose OPT evicts page x, whose next request occurs farthest in the future and A evicts page y instead.    

Because OPT selected the page with the farthest future use, next(x) ≥ next(y).  

Modify algorithm A so that it evicts x instead of y, which does not increase the number of cache misses because page y will be needed sooner and keeping y in cache avoids a potetntial earlier miss.   

Then, misses(OPT) ≤ misses(A) for any algorithm A on the same request sequence.
So, OPTFF is optimal.