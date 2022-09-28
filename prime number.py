# prime number using flag:

def prime_number(n):
    flag=False
    if n>1:
        for i in range (2,n):
            if n%i==0:
                flag=True
                break
        if flag:
            return"n0! its not a prime number"
        else:
            return "yes! its a prime number"
print(prime_number(6))


# a=[1,2,3,5,8,4]
# i=0
# while i<len(a):
#     j=1
#     count=0
#     while j<=a[i]:
#         if a[i]%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print(a[i],"It is a prime number")
#     else:  
#         print(a[i],"is not a prime number")
#     i+=1