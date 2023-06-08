l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)


k=2
m = []
for i in range(len(l)): 
   if l[i] < k:
      m.append(l[i]+k)
   else:
      m.append(l[i]-k)
print(m)

mini = min(m)
maxi = max(m)
final = mini+maxi
print(final)

