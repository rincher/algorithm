class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if not stack or stack[-1] == "[" or stack[-1] == "{":
                    return False
                    break
                elif stack[-1] == "(":
                    stack.pop()
            elif i == "]":
                if not stack or stack[-1] == "(" or stack[-1] == "{":
                    return False
                    break
                elif stack[-1] == "[":
                    stack.pop()
            elif i == "}":
                if not stack or stack[-1] == "(" or stack[-1] == "[":
                    return False
                    break
                elif stack[-1] == "{":
                    stack.pop()
        if stack:
            return False
        else:
            return True
