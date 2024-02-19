
var = input("palabra : ")
a = ""
b =["a","e","i","o","u"]
for i in var :
    if i.lower() not in b :
        a = a + i
print(a)
