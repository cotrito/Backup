import sys
import csv
import tabulate
import json
from datetime import datetime

def main():
    """menu options"""
    option = input('1 - Show menu\n2 - New table order\n3 - Close table\n4 - Show payments\n5 - Exit\n')
    if option =='1':
        menu = show_menu()
        print(tabulate.tabulate(menu, headers="firstrow", tablefmt="github"))
    elif option =='2':
        order()
    elif option =='3':
        calculate_total()
    elif option =='4':
        pay = show_payments()
        print(tabulate.tabulate(pay, headers="firstrow", tablefmt="github"))
    elif option =='5':
        sys.exit('Exiting')
    else :
        sys.exit('Invalid option')

def show_payments():
    pay =[]
    with open('payments.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            pay.append({"Table": row[0], "Total": row[1], "Date": row[2], "Time": row[3]})
        return pay

def show_menu():
    menu =[]
    with open('menu.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append({"Id": row[0], "Item": row[1], "Price": row[2]})
        return menu

def write_order(table,item,qty):
    with open ('tables.json','r+') as file2:
        new_data ={"Item_id":item,"Cuantity":qty}
        file_data = json.load(file2)
        file_data["Tables"][f'table{table}']["orders"].append(new_data)
        file2.seek(0)
        json.dump(file_data,file2)

""" look if table is created in tables.json file """
def table_exist(table):
    with open ('tables.json','r') as file2:
        file_data = json.load(file2)
        try :
            file_data["Tables"][table]
            return True
        except KeyError:
            print('Table dont exist')

def chose_table():
    is_table = False
    while is_table == False:
        table = input('Input n° table: ')
        if table_exist(f'table{table}') == True :
            is_table = True
            return(table)

def calculate_total():
    total = 0
    table = chose_table()
    reader = show_menu()
    with open ('tables.json','r') as file2:
        file_data = json.load(file2)
        orders = file_data["Tables"][f'table{table}']['orders']
        for order in orders:
            id = int(order["Item_id"])
            price = float(reader[id]['Price'])
            qty = int(order["Cuantity"])
            total = total + (price * qty)
        if total == 0:
            print('Total is 0, cannot close the table')
        else :
            print(f'The total is {total}')
            ans = input('Table was paid (yes or no): ')
            if ans =='yes':
                print('Errasing')
                errase_table_orders(table)
                save_total(total,table)

def errase_table_orders(table):
    with open ('tables.json','r') as file2:
        file_data = json.load(file2)
        file_data["Tables"][f'table{table}']["orders"] = []
    with open ('tables.json','w') as file2:
        json.dump(file_data, file2)

def save_total(total,table):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")
    reg = [table,total,current_date,current_time]
    with open('payments.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(reg)

def order():
    i = 0
    table = chose_table()
    while i == 0:
        ids =[]
        menu = show_menu()
        for x in range(len(menu)) :
            ids.append(menu[x]["Id"])
        print('')
        print(tabulate.tabulate(menu, headers="firstrow", tablefmt="github"))
        print('')
        add = input('Insert id of food to add or input 0 for exit: ')
        if add == '0':
            i = 1
        elif add == 'id':
            print('Item id not available')
        elif add in ids:
            ind = ids.index(add)
            num = input(f'How many {menu[int(ind)]["Item"]} do you want to add to table {table}\ninput 0 if selected the wrong id\n: ')
            try:
                if int(num) >0 and int(num) <=10 :
                    print(f'Adding {num} {menu[int(add)]["Item"]} to table {table}')
                    write_order(table,add,num)
                elif int(num) == 0 :
                    print('Cant add 0')
                elif int(num) >10 :
                    print('Max quantity is 10 units')
            except ValueError:
                print('Not a valid quantity')
        else :
            print('Item id not available')

if __name__ == "__main__":
    main()

