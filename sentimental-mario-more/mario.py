from cs50 import get_int

h = 0

while h < 1 or h >8 :
    h = get_int("height : ")

for i in range(1,h+1):
    f = h - i
    print(" "*f, end ="")
    print("#"*i, end ="")
    print(" "*2, end ="")
    print("#"*i)
