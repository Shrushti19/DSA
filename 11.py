l = []

n = int(input("Enter the number of elements "))
for i in range(n):
   a = int(input())
   l.append(a)
print(l)

for i in range(len(l)):
  l1 = 0
  for j in range(len(l)):
     if i == j:
        l1+=1
     
print("The most repeated digit is ",i )
print(l1)
