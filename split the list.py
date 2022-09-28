# str="a,a,a,b,b,c,c,c"
# output= a:3,b:2,c:3
# output=['a','a','a','b',b','c','c','c']

str="a,a,a,b,b,c,c,c"
a=str.split(',')
print(a)
# output=['a','a','a','b',b','c','c','c']


str="a,a,a,b,b,c,c,c" 
a=str.split(',')
b=[]
new_list=[]
for ch in a:
    if ch not in b:
        new_list.append(f"{ch}:{a.count(ch)}")
        b.append(ch)
print(new_list)
print(",".join(new_list))

# # string
# str1=input("enter string:")
# b=""
# for char in str1:
#     if chr.isalpha():
#         var=char
#     else:
#         num=int(char)
#         b=b+(var*num)
# print(b)
        