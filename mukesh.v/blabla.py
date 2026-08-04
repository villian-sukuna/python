class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
           
        b=str(x)
        c=b[::-1]
        if b!=c:
            print(c)
        return 0
s=Solution()
s.reverse(x=-123)