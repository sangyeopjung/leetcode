# https://leetcode.com/problems/accounts-merge/description/
# tags: union find, dsu

class DSU:
    def __init__(self):
        self.parent = {} # a@b.com -> z@b.com
        self.size = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
        elif self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y): # join x on y
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False

        if self.size[xp] >= self.size[yp]:
            self.size[xp] += self.size[yp]
            self.parent[yp] = xp
        else:
            self.size[yp] += self.size[xp]
            self.parent[xp] = yp
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}

        for emails in accounts: # [John, a@b.com, b@b.com, ..., z@b.com]
            name = emails[0]
            for i in range(1, len(emails)):
                dsu.union(emails[i], emails[1])
                email_to_name[emails[i]] = name
        
        emails = defaultdict(list)
        for email, _ in dsu.parent.items():
            emails[dsu.find(email)].append(email)
        
        out = []
        for key, emaillist in emails.items():
            account = [email_to_name[key]]
            emaillist.sort()
            for email in emaillist:
                account.append(email)
            out.append(account)
        
        return out