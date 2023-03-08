# https://leetcode.com/problems/top-k-frequent-words/description/
# tags: heap

class Pair:
    def __init__(self, word, freq):
        self.word = word 
        self.freq = freq 
    
    def __lt__(self, p):
        return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = defaultdict(int)
        for word in words:
            m[word] += 1

        heap = [] # min heap
        for word, freq in m.items():
            if len(heap) < k:
                heappush(heap, Pair(word, freq))
            else:
                heappushpop(heap, Pair(word, freq))
        
        return [pair.word for pair in sorted(heap, reverse=True)]