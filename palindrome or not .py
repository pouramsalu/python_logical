


def palindrome(s):
    temp=s[::-1]
    if s ==temp:
        print("yes! its a palindrome")
    else:
        print("no! its not a palindrome")  
s="nitin"
palindrome(s)

# by using indexing/using for loop

def palindrome(s):
    n=len(s)
    for i in range (n):
        if s[i]!=s[n-i-1]:
            return False
        return True
s="wnitinw"
print(palindrome(s))

# reverse and join./inbuilt function

# def palindrome(s):
#     temp="".join(reversed(s))
#     if s==temp:
#         return True
#     else:
#         return False
# s="wnitinw"
# print(palindrome(s))

# by using while loop

def palindrome(n):
    temp=n
    rev_n=0
    while (temp>0):
        digit=temp%10
        rev_n=rev_n*10+digit
        temp=temp//10
    if n==rev_n:
        return True
    else:
        return False
n=12345643221
print(palindrome(n))
