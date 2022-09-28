# Notify string formate
# input=I_aM_Coder
# output=i.aM.a. coDER

def string_formate(s):
    a=[]
    temp=s.split(',')
    for i in temp:
        a.append(i[0].lower()+i[1:].upper())
    s=','.join(a)
    print(s)
s="I_aM_Coder"
string_formate(s) 



