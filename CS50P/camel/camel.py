val = input("palabra : ")
a = ""
for i in val :
    if i.isupper() == True :
        a = a + "_" + i.lower()
    else :
        a = a + i
print(a)