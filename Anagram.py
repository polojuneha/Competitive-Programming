S1 = str(input("enter string 1:"))
S2 = str(input("enter string 2:"))
a = S1.lower()
b = S2.lower()
P1 = sorted(a)
P2 = sorted(b)
k1 = len(P1)
k2 = len(P2)
K1 = []
K2 = []
for i in range(k1):
	if(P1[i]!=" "):
		K1.append(P1[i])
for i in range(k2):
	if(P2[i]!=" "):
		K2.append(P2[i])
c = len(K1)
d = len(K2)
# print(str(K1))
if(str(K1) == str(K2)):
	print("True")
else:
	print("False")
# print(K1)
# print(K2)
# count = 0
# if(c==d):
# 	for i in range(c):
# 		if(K1[i] == K2[i]):
# 			count = 0
# 		else:
# 			count = 1
# 	if(count == 0):
# 		print("True")
# 	else:
#  		print("False")
# else:
# 	print("False")

# L1 = list(S1)
# L2 = list(S2)
# K1 = L1.sort()
# k = len(K1)
# print(L1)
# K2 = L2.sort()
# print(L2)
# for i in range(k):
# 	if(k1[i] == k2[i]):
# 		print("True")
# 	else:
# 		print("False")