def main():
    val = input("Greeting:" )
    print(f'${value(val)}')

def value(greeting):
    greeting = greeting.lower().strip()
    pri = greeting[0]
    wor = greeting[0:5]
    if wor =="hello" :
        return 0
    elif pri =="h":
        return 20
    else :
        return 100

if __name__ == "__main__":
    main()



