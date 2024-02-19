def main():
    x=listado()
    x = sorted(x)
    my_dict ={i:x.count(i) for i in x}
    for s in my_dict :
        print(f"{my_dict[s]} {s}")

def listado():
    lis=[]
    while True:
        try :
           lis.append(input().upper())
        except EOFError:
            break
    return lis


main()