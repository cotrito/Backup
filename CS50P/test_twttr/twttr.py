def main():
    var = input("palabra : ")
    print(shorten(var))

def shorten(word):
    a = ""
    b =["a","e","i","o","u"]
    for i in word :
        if i.lower() not in b :
            a = a + i
    return a

if __name__ == "__main__":
    main()