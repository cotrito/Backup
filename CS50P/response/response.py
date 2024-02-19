from validator_collection import checkers

def main():
    print(response(input('email: ')))

def response(s):
    if checkers.is_email(s) == True:
        return 'Valid'
    else :
        return 'Invalid'

if __name__ == "__main__":
    main()