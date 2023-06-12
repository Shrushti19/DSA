l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)

l1 = []

m = int(input("Enter the number of elements "))
for i in range(m):
   a = int(input())
   l1.append(a)
print(l1)

w = l  + l1
print("Merge list is ",w)
w.sort()
print("Sorted list is ",w)


a = w[0:n]
print(a)

b = w[n:]
print(b)
