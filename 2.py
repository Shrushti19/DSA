l = []
n = int(input("Enter the number of ele "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)

m = 0
print("Max element in array is ")
for i in l:
   m = max(l)
print(m)

s = 0
print("Min element in array is ")
for i in l:
   s = min(l)
print(s)
