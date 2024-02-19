import sys

if len(sys.argv) > 2 :
    sys.exit("to many arguments")
elif len(sys.argv) < 2:
    sys.exit("to few arguments")
elif sys.argv[1][-3:] != '.py' :
    sys.exit("not a python program")
else:
    file_name = sys.argv[1]
    try :
        with open(file_name, "r") as file:
            i=0
            for line in file:
                if line.rstrip() =="":
                    i = i
                elif line.rstrip().strip()[0] == "#":
                    i = i
                else :
                    i+=1
            print(i)
    except FileNotFoundError:
        sys.exit("File does not exist")
sys.exit()


