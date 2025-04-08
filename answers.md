# CMPS 2200 Assignment 3
## Answers

**Name:** Samuel Kelly

**1a)** 
For an amount N dollars, the most efficient approach to minimize coin count involves prioritizing higher denomination coins first. This strategy proceeds by using the maximum possible quantity of the largest value coin, then moving to the next largest denomination when necessary. This process continues sequentially until we reach exactly N dollars, which is guaranteed because a 1-unit coin exists in the system.

**1b)**
This approach is demonstrably optimal because using multiple coins of any denomination would be inefficient compared to substituting them with a larger denomination coin whenever possible. This exemplifies the core principle of greedy algorithms: always selecting the highest available denomination represents the most efficient choice at each step.

**1c)**
The computational complexity of this solution yields both work and span of log(n). This occurs because each time we add a coin, we effectively reduce the remaining amount by a factor of 2, essentially performing a binary decomposition of the total value.

**2a)**
In Fortuito's currency system, the greedy approach fails to produce optimal results. Consider a system with denominations of 4, 3, and 1. To represent 6 units using the greedy method, we would select one 4-unit coin plus two 1-unit coins (total: 3 coins). However, the truly optimal solution would be two 3-unit coins (total: 2 coins).

**2b)**
While this problem lacks the greedy choice property, it does exhibit optimal substructure. This property manifests because finding the minimum number of coins can be decomposed into smaller, related subproblems—a hallmark of optimal substructure. When evaluating a specific denomination (Dk), we face two choices: either include it, transforming our problem C(N,k) into C(N-Dk,k)+1, or exclude it, yielding C(N,k-1). By recursively exploring all possibilities while employing memoization to avoid redundant calculations, we can determine the minimum coin count. This recursive breakdown confirms the problem's optimal substructure.

**2c)**
Utilizing the optimal substructure property, we can implement a dynamic programming solution. The algorithm considers N+1 distinct amounts (from 0 to N) across k+1 different coin types (from 0 to k). Each subproblem requires O(1) work for minimization operations. Therefore, the total computational complexity for both work and span is O(Nk), reflecting the need to evaluate all possible combinations of amounts and denomination types.

