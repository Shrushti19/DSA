l1 = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l1.append(a)
print(l1)

l2 = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l2.append(a)
print(l2)


l = []

for i in range(len(l1)):
  for j in range(len(l2)):
     if l1[i] == l2[j]:
        l.append(l1[i])
print(l)


u = list(set(l1) | set(l2))
print(u)


