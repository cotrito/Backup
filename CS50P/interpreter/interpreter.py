var = input("input: ")
pos = var.find(" ")
pos2 = var.rfind(" ")+1
a = float(var[0:pos].strip())
b = var[pos+1:pos2].strip()
c = float(var[pos2:].strip())

if b=="+":
    print(a + c)
elif b=="-":
    print(a - c)
elif b=="*":
    print(a * c)
elif b=="/":
    print("%.1f" % (a / c))
