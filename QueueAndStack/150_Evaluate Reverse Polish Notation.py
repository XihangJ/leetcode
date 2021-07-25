'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_nums = []
        ops = {'+', '-', '*', '/'}
        for curr in tokens:
            if curr not in ops:
                stack_nums.append(int(curr))
            else:
                num2 = stack_nums.pop()
                num1 = stack_nums.pop()
                if curr == '+':
                    num = num1 + num2
                elif curr == '-':
                    num = num1 - num2
                elif curr == '*':
                    num = num1 * num2
                else:
                    num = math.trunc(num1 / num2)
                stack_nums.append(num)
        return stack_nums[0]
