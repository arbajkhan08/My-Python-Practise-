
"""def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("enter the nnumber"))
b = int(input("enter the nnumber"))
c = int(input("enter the nnumber"))
  
print(greatest(a,b,c))    """

'''def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4)) '''



'''def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    pattern(n-1)


pattern(5)  '''


'''def inch_to_cms(inch):
    return inch * 2.54

n= int(input("ente the value in inches")) '''

'''def rem(l, word):
    n = []
    for item in l :
        
        if not(item == word):
            n.append(item.strip(word))
        return n
 

l = ["artbaj ", "harry", "rohan"]
print(rem(l, "ar"))'''


def multiply(n):
    for i in range(1, 11):
      print(f"{n} x {i} =  {n*i}")

multiply(6)    