class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        braces = {"}": "{", ")": "(", "]": "["}

        for character in string:
            if character in braces.values():
                stack.append(character)
            elif character in braces.keys():
                try:
                    if braces[character] != stack.pop():
                        return False
                except IndexError:
                    return False

        return not stack
