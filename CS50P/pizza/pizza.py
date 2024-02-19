import sys
import csv
import tabulate

pizza = []
if len(sys.argv) > 2 :
    sys.exit("to many arguments")
elif len(sys.argv) < 2:
    sys.exit("to few arguments")
elif sys.argv[1][-4:] != '.csv' :
    sys.exit("not a csv file")
else:
    file_name = sys.argv[1]
    try :
        with open(file_name) as file:
            #reader = csv.DictReader(file)
            reader = csv.reader(file)
            for row in reader:
                #pizza.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
                pizza.append({"item": row[0], "Small": row[1], "Large": row[2]})
        print(tabulate.tabulate(pizza, headers="firstrow", tablefmt="grid"))
        #print(tabulate.tabulate(pizza, headers=["Sicilian Pizza","Small","Large"], tablefmt="plain"))
        #print(pizza)
    except FileNotFoundError:
        sys.exit("File does not exist")