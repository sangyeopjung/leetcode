# https://leetcode.com/problems/basic-calculator-ii/description/
# tags: calculator, stack, parsing

class Solution:
    def evaluate(self, stack, oper, num):
        if oper == '+':
            stack.append(num)
        elif oper == '-':
            stack.append(-num)
        elif oper == '*':
            stack[-1] *= num
        else:
            stack[-1] = int(stack[-1] / num)

    def calculate(self, s: str) -> int:
        stack = []
        oper, num = '+', 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in ['+', '-', '*', '/']:
                self.evaluate(stack, oper, num)
                oper, num = c, 0
        self.evaluate(stack, oper, num)
        return sum(stack)



class Solution:
    def evaluate(self, out, last, oper, num):
        if oper == '+':
            return out + last, num
        elif oper == '-':
            return out + last, -num
        elif oper == '*':
            return out, last * num
        else:
            return out, int(last / num)

    def calculate(self, s: str) -> int:
        out = last = 0
        oper, num = '+', 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in ['+', '-', '*', '/']:
                out, last = self.evaluate(out, last, oper, num)
                oper, num = c, 0
        out, last = self.evaluate(out, last, oper, num)
        return out + last
