class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #Xác định dấu
        if x >= 0:
            neg = 1
        else:
            neg = -1
        x *= neg
        num = 0
        while x:
            num = num*10 + x%10#Lấy phần dư
            x //= 10#lấy phần nguyên

        num *= neg
        if num > (2**31) - 1 or num < -1*(2**31):
            return 0
        return num