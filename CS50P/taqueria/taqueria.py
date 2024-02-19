menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True :
    try :
        z = str.title(input("Item : ").lower())
        #print(menu[z])
        total = total + menu[z]
        v_total = "{:.2f}".format(total)
        print(f"Total: ${v_total}")
    except KeyError:
        pass
    except :
        break