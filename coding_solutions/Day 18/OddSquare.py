lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
for num in lst: 
    if num % 2 != 0: 
       print(num*num, end = " ")