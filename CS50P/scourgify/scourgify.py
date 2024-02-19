import sys
import csv

lista=[]

if len(sys.argv) > 3 :
    sys.exit("to many arguments")
elif len(sys.argv) < 3:
    sys.exit("to few arguments")
elif sys.argv[1][-4:] != '.csv' :
    sys.exit("input not a csv file")
elif sys.argv[2][-4:] != '.csv' :
    sys.exit("output not a csv file")
else:
    file_name = sys.argv[1]
    try :
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name , name = row["name"].split(",")
                lista.append({'first' : name.lstrip(),'last' : last_name.lstrip(),'house' : row["house"]})

        with open(sys.argv[2], "w") as file2:
            writer = csv.DictWriter(file2, fieldnames=["first","last","house"])
            writer.writeheader()
            for row in lista:
                writer.writerow({"first":row['first'],"last":row['last'],"house":row['house']})

    except FileNotFoundError:
        sys.exit("File does not exist")