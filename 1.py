l = []
l1 = []

n = int(input("Enter the elements in the array "))
for i in range(n):
   a = int(input())
   l.append(a)
   
print(l)

print("Reverse array is ")
for i in l:
   l1 = l[::-1]
   
print(l1)
