class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            try:
                token = int(token)
                stack.append(token)
            except:
                operand2 = stack.pop()
                operand1 = stack.pop()
                match token:
                    case "+":
                        res = operand1 + operand2
                        stack.append(res)
                    case "-":
                        res = operand1 - operand2
                        stack.append(res)
                    case "/":
                        res = int(operand1 / operand2)
                        stack.append(res)
                    case "*":
                        res = operand1 * operand2
                        stack.append(res)
        return stack[-1]
        