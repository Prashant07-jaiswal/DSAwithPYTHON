class Solution:
    def palindrom(self,x):
        if x<0:
            return False
        rev = 0
        temp = x 
        while temp != 0:
            digit = temp%10
            rev = (rev*10) + digit
            temp = temp // 10
        if rev == x:
            return True
        else:
            return False



obj = Solution()
print(obj.palindrom(-121))