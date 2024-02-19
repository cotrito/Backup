from pyfiglet import Figlet
import random
figlet = Figlet()
import sys

a = figlet.getFonts()

if len(sys.argv) == 1:
    random.shuffle(a)
    f = a[0]
elif (len(sys.argv) == 3) and (sys.argv[1] == '-f' or sys.argv[1] =='--font'):
    if sys.argv[2] in a :
        f = sys.argv[2]
    else :
        sys.exit("error")
else :
    sys.exit("error")

s =input('Input : ')
figlet.setFont(font=f)
print(figlet.renderText(s))
