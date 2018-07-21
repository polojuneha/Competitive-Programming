class Solution:
   def binaryGap(self, N):
       last = None
       result = 0
       for i in range(32):
           if (N >> i) & 1:
               if last is not None:
                   result = max(result, i - last)
               last = i
       return result
x=Solution()
print(x.binaryGap(0))
print(x.binaryGap(55))
print(x.binaryGap(-5))
print(x.binaryGap(12354))
print(x.binaryGap(6))
print(x.binaryGap(256))