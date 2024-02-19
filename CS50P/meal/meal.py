def main():
    time = input("what time is it : ")
    res = convert(time)
    if res >=7 and res <=8 :
        print("breakfast time")
    elif res >=12 and res <=13 :
        print("lunch time")
    elif res >=18 and res <=19 :
        print(" dinner time")

def convert(time):
    pos = time.find(":")
    a= int(time[0:pos])
    b= float(time[pos+1:])/60
    c= a+b
    return c

if __name__ == "__main__":
    main()