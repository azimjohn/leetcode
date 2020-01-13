class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        result = None

        for token in tokens:
            if token not in ["*", "/", "+", "-"]:
                stack.append(token)
                continue
            
            operator = token
            operand_two = int(stack.pop())
            operand_one = int(stack.pop())
            
            if operator == "+":
                result = operand_one + operand_two
            elif operator == "-":
                result = operand_one - operand_two
            elif operator == "*":
                result = operand_one * operand_two
            elif operator == "/":
                result = operand_one / operand_two

            stack.append(int(result))
        
        if stack:
            return stack.pop()

        return result
