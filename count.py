# count the alphabet by using for loop

# def compress(s):
#     n=len(s)
#     new_s=" "
#     count=1
#     for i in range(n-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             new_s=new_s+s[i]+str(count)
#             count+=1
#     new_s=new_s+s[n-1]+str(count)
#     return new_s
# s="aabbccaaaff"
# print(compress(s))


# by using while loop

def compress(s):
    n=len(s)
    i=0
    new_s=" "
    while (i<n-1):
        count=1
        while (i<n-1 and s[i]==s[i+1]):
            count+=1
            i+=1
        i+=1
        new_s=new_s+s[i-1]+str(count)
    return new_s
s="nnnnnniiiittttiiinnn"
print(compress(s))

     