l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)

sum = 0
maxsum = []
for i in l:
   sum+=i
   maxsum.append(sum)
print(max(maxsum))




