class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res=""
        n1=len(num1)
        n2=len(num2)
        c=0
        if(n1>n2):
            num2=("0"*(n1-n2))+num2
        else:
            num1=("0"*(n2-n1))+num1
        # print(num1, num2)
        for i in range(len(num1)):
            a=ord(num1[-i-1])
            b=ord(num2[-i-1])
            d=a+b+c-96
            if(d>9):
                c=d//10
            else:
                c=0
            res=(str(d-c*10))+res
            # print(a, b, d-c*10, c)
        if(c>0):
            res=str(c)+res
        return res
        