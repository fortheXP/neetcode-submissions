class Solution:
    def isPalindrome(self, s: str) -> bool:
        checklist = []
        for i in s:
            if i.isalnum():
                checklist.append(i.lower())
        
        return checklist == checklist[::-1]