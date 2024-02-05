from typing import List


class Solution:
    def calc(self, x, y, operation):
        match operation:
            case '+':
                return x + y
            case '-':
                return y - x
            case '*':
                return x * y
            case '/':
                return int(y / x)

    def evalRPN(self, tokens: List[str]) -> int:
        _stack = []
        _operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in _operators:
                _stack.append(self.calc(_stack.pop(), _stack.pop(), token))
            else:
                _stack.append(int(token))
        return _stack.pop()


s = Solution()
# print(s.evalRPN(["2", "1", "+", "3", "*"]))
# print(s.evalRPN(["2", "1", "-", "3", "*"]))
# print(s.evalRPN(["4", "13", "5", "/", "+"]))
# print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(s.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]))
