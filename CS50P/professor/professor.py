import random
import sys
def main():
    score = 0
    lvl =int(get_level())
    if lvl ==1:
        level =[0,9]
    elif lvl ==2:
        level =[10,99]
    else :
        level =[100,999]

    for i in range (10):
        quest = generate_integer(level)
        cont = 0
        while True:
            ans = input(quest[0])
            if cont == 2:
                print(str(quest[0]) + str(quest[3]))
                break
            elif ans == str(quest[3]):
                score = score + 1
                break
            else :
                print('EEE')
                cont = cont + 1
                pass
    print(f'score: {score}')
    #sys.exit(f'score: {score}')
    return score

def get_level():
    while True:
        level = input("Level: ")
        if level =='1' or level =='2' or level =='3':
            return level
        else :
            pass


def generate_integer(level):
    num1 = random.randint(level[0],level[1])
    num2 = random.randint(level[0],level[1])
    result = num1 + num2
    txt = str(num1)+' '+'+'+' '+str(num2)+' = '
    return txt, num1, num2, result

if __name__ == "__main__":
    main()
