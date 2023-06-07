l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)

kth = int(input("Enter the position of min to find "))
for i in l:
  l.sort()
  m = l[kth-1]
print(m)
