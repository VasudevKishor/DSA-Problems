class Solution(object):
    def isPalindrome(self, x):
        if x < 0:  
            return False
        lst = []
        while x != 0:
            val = x % 10  
            lst.append(val)  
            x //= 10  
        length = len(lst)
        for i in range(length // 2):
            if lst[i] != lst[length - 1 - i]:
                return False
        return True 
