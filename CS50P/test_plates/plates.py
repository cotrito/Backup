
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    y =[]
    j =[]
    k = len(s)
    for i in s :
        y.append(i.isalpha())
        j.append(i.isalnum())


    if y[0] == False or y[1] == False :
        return False
    elif k != sum(j) :
        return False
    elif k <2 or k >6 :
        return False
    elif k == sum(y) :
        return True
    elif k != sum(y) :
        q = y.index(False)
        if sum(y[q:]) > 0:
            return False
        elif s[q] == "0" :
            return False
        else :
            return True
    else :
        return True


if __name__ == "__main__":
    main()
