l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)


l1 = [l[len(l)-1]]
for i in range(len(l)-1):
   l1.append(l[i])
print(l1)
