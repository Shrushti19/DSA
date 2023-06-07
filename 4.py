l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)

l1 = []
for i in l:
   if l[i] == 0:
      l1.append(l[i])
      
for i in l:
   if l[i] == 1:
      l1.append(l[i])
      
for i in l:
   if l[i] == 2:
      l1.append(l[i])

print(l1)
