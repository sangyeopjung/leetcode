# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# tags: design, trie, dfs

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True

    def search(self, word: str) -> bool:
        def dfs(node, depth=0):
            if depth == len(word):
                return '$' in node

            c = word[depth]
            if c == ".":
                for char, child in node.items():
                    if char != '$' and dfs(child, depth+1):
                        return True
            else:
                if c in node and dfs(node[c], depth+1):
                    return True
            
            return False
        
        return dfs(self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)