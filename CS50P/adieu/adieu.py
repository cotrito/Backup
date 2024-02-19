a =[]
b = 'Adieu, adieu, to '
while True:
    try:
        a.append( input())
    except EOFError:
        break

if len(a)== 2:
    b = b + a[-2]+ ' and '+ a[-1]
else:

    for i in range (len(a) -1):
        b = b + a[i] + ', '
    if len(a)== 1:
        b = b + a[-1]
    else :
        b = b + 'and '+ a[-1]
print(b)