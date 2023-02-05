```
class Solution:
def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
n = len(words)
ans = []
prefix = [0] * (n + 1)
vowels = {'a', 'e', 'i', 'o', 'u'}
good = {i for i in range(len(words)) if words[i][0] in vowels and words[i][-1] in vowels}
for i in range(n):
prefix[i+1] = prefix[i] + (1 if i in good else 0)
for l,r in queries:
ans.append(prefix[r + 1] - prefix[l])
return ans
```
​
The key concept here is the [prefix sum](http://en.wikipedia.org/wiki/Prefix_sum). The prefix sum is a second array that keeps track of the running total of an input sequence. This can be used for fast lookup calculations.
Since queries are contiguous ranges, we can keep track of an array, prefix, of size n+1, such that each element at index i is the number of words before i that meet the vowel criteria, with the last element being the number of overall words that meet the criteria. We precompute the values of this by creating a set of indexes where our criteria for the element is met. This may make it faster, not sure.
When calculating the answer, we take prefix[l] of the query, that is, the number of elements before index l that meet the criteria and subtract that from prefix[r+1], the number of elements before r+1 that meet the criteria.