class Solution(object):
    def hammingDist(self, x, y):
        biX = bin(x)[2:]
        biY = bin(y)[2:]
        l = min(len(biX),len(biY))
        k = max(len(biX),len(biY))
        if len(biX)<=len(biY):
            biX = '0'*(k-l) + biX
        else:
            biY = '0'*(k-l) + biY
        m = 0
        for i in range(k):
            if biX[i] != biY[i]:
                m += 1
        return m
x = 1
y = 4
z = Solution()
print(z.hammingDist(x,y))
a = 25
b = 30
print(z.hammingDist(a,b))
c = 100
d = 250
print(z.hammingDist(c,d))
e = 1
f = 30
print(z.hammingDist(e,f))
g = 0
f = 255
print(z.hammingDist(g,f))