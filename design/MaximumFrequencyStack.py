# https://leetcode.com/problems/maximum-frequency-stack/description/
# tags: design, stack

class FreqStack:

    def __init__(self):
        self.stacks = defaultdict(list) # stacks[freq] = [values]
        self.freqs = defaultdict(int) # freqs[value] = freq
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freqs[val] += 1
        self.maxfreq = max(self.maxfreq, self.freqs[val])
        self.stacks[self.freqs[val]].append(val)

    def pop(self) -> int:
        val = self.stacks[self.maxfreq].pop()
        if not self.stacks[self.maxfreq]:
            self.maxfreq -= 1
        self.freqs[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()