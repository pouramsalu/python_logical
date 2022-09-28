
# def armstrong(n):
#     sum=0
#     temp=n
#     while temp>0:
#         digit=temp%10
#         sum=sum+(digit**3)
#         temp=temp//10
#     if n==sum:
#         print("yes")
#     else:
#         print("no")
# n=371
# armstrong(n)

# print list of armstrong number for a particular intervel

def armstrong(start,end):
    for n in range(start,end):
        sum=0
        temp=n
        while temp>0:
            digit=temp%10
            sum=sum+(digit**3)
            temp=temp//10
        if n==sum:
            print(n)
armstrong(0,500)