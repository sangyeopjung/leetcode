# https://leetcode.com/problems/task-scheduler/description/
# tags: array, greedy

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # you can either fill the CPU entirely, in which case the answer is tasks.size()
        # if you cannot fill the CPU entirely, it depends on the largest frequency element
        freq = [0 for _ in range(26)]
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        maxfreq = max(freq)
        out = (maxfreq - 1) * (n + 1)
        for f in freq:
            if f == maxfreq:
                out += 1

        return max(out, len(tasks))
