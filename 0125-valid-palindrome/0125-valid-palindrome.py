class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if s == s[::-1]:
            return True
        else: 
            return False
        