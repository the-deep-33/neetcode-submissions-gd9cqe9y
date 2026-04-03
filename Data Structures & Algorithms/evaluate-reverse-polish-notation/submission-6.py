class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                if i == "+":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    temp = temp1 + temp2
                    stack.append(temp)
                elif i == "-":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    temp = temp2 - temp1
                    stack.append(temp)
                elif i == "*":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    temp = temp2 * temp1
                    stack.append(temp)
                elif i == "/":
                    temp1 = stack.pop()
                    temp2 = stack.pop()
                    temp = int(temp2 / temp1)
                    stack.append(temp)

        return stack[0]
        