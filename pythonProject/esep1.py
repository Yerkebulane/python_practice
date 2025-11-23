# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         if i>=0:
#             print(i**2)

n = int(input())

arr=[]

for i in range(n):
    elem = int(input('elem' + i + ': '))
    arr.append(elem)
    
print(arr)