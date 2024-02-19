from cs50 import get_string
import sys

def main():
    while True :
        try:
            tc = get_string("credit card number : ")
            lc = len(tc)
            if(valid(tc,lc)):
                card = name(tc,lc)
                print(f"{card}")
                sys.exit(0)
            else :
                print("INVALID")
                sys.exit(0)

        except ValueError:
            main()

def valid(tc,lc):
    if(lc % 2) == 0:
        pos = 0
    else:
        pos = 1

    ttl = 0

    for le in tc:
        if(pos % 2) == 0:
            nle = str(int(le)*2)
            for n in nle:
                ttl += int(n)
        else:
            ttl += int(le)

        pos +=1
    #print(f"{ttl % 10}")
    if ttl % 10 == 0 :
        return True
    else:
        return False


def name(tc,lc):
    tc = int(tc)
    card = 'INVALID'
    if lc == 15 :
        ini = int(tc/10000000000000)

        if ini in [34,37]:
            card = 'AMEX'
    elif lc == 13 :
        ini = int(tc/1000000000000)
        if ini == 4:
            card = 'VISA'
    elif lc == 16 :
        ini = int(tc/1000000000000000)
        ini2 = int(tc/100000000000000)
        #print(f"{ini2}")
        if ini == 4:
            card = 'VISA'
        elif ini2 in range(51,56) :
            card = 'MASTERCARD'
    return card


main()
