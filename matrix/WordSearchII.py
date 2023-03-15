# https://leetcode.com/problems/word-search-ii/
# tags: matrix, trie, backtracking

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = word

        out = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    self.dfs(board, i, j, trie[board[i][j]], out)
        return out

    # invariants: i,j are in range; node is the current char; not explored yet
    def dfs(self, board, i, j, node, out):
        c = board[i][j]
        # exploring...
        board[i][j] = '#'
        if '$' in node: # reached a valid word
            out.append(node['$'])
            del node['$']
        
        # explore each valid neighbour
        for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            x, y = i+dx, j+dy
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) \
                    and board[x][y] in node and board[x][y] != '#':
                self.dfs(board, x, y, node[board[x][y]], out)
        
        # backtrack
        board[i][j] = c
