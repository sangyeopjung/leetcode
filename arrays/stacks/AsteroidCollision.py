# https://leetcode.com/problems/asteroid-collision/description/
# tags: stack

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] == -a:
                    stack.pop()
                    break
                elif stack[-1] < -a:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(a)

        return stack