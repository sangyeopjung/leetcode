# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# tags: two pointers

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        curmax = 0 # current maximum frequency
        l = 0 # sliding window
        for r in range(len(s)):
            freq[s[r]] += 1 # increase the frequency of char
            curmax = max(curmax, freq[s[r]]) # we never have to decrease this; only interested in max
            if r - l + 1 > curmax + k: # window is bigger than most frequent + k
                freq[s[l]] -= 1 # need to shift left ptr and decrease its corresponding freq
                l += 1
        return len(s) - l # size of the window when the right ptr reaches the end
