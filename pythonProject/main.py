from random import randint
c = []
t = []
a = [[randint(-20,20) for i in range(3)] for j in range(3)]
for i in a :
    if a[i]%2==1:
        c = i.append
        
    

print(c)

n = int(input)
if n%2==1:
    print("Werid")
elif n%2==0 and n>1 and n<6 :
    print("Not Werid")
elif n%2==0 and n>5 and n<21:
    print("Werid")
elif n%2==0 and n>20 :
    print("Not Werid")
    