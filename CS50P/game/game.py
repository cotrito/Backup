import random
import sys

def main():

    while True:
        var = input("level: ")
        try:
            var = int(var)
            if var > 0 :
                break
            else :
                pass

        except ValueError:
            pass
        except EOFError:
            break

    level = random.randrange(1,var+1)
    print(level)

    while True:
        var2 = input("Guess: ")
        try:
            var2 = int(var2)
            if var2 > 0 :
                if var2 ==  level:
                    sys.exit("Just right!")

                elif var2 <  level:
                    print("Too small!")
                    pass

                elif var2 > level:
                    print("Too large!")
                    pass
                else:
                    pass
            else :
                pass

        except ValueError:
            pass
        except EOFError:
            break

main()