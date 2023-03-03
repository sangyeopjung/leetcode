# https://leetcode.com/problems/word-ladder/
# tags: bfs,  string, search

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                adj[word[:i] + '.' + word[i+1:]].append(word)
        
        queue = deque([beginWord])
        visited = set()
        depth = 0
        while len(queue):
            depth += 1
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return depth
                
                if word in visited:
                    continue
                visited.add(word)
                
                for i in range(len(beginWord)):
                    wildcard = word[:i] + '.' + word[i+1:]
                    for neighbour in adj[wildcard]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                    adj[wildcard].clear()
        
        return 0
