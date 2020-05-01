class Solution:
    def checkValidString(self, s: str) -> bool:
        if not self.checkValid(s, '('):
            return False
        
        if not self.checkValid(reversed(s), ')'):
            return False
        
        return True
    
    def checkValid(self, s, open_parenthesis):
        balance = 0
        for char in s:
            if char in [open_parenthesis, '*']:
                balance += 1
            else:
                balance -= 1

            if balance == -1:
                return False
        return True
