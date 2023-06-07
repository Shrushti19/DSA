l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)

l1 = []
for i in l:
   if i < 0:
      l1.append(i)
      
for i in l:
   if i >= 0 :
      l1.append(i)
      

print(l1)
