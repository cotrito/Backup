var = 50
while var > 0 :
    print("amount due: " + str(var))
    x = int(input("moneda : "))

    if x == 25 :
        var = var - 25
    elif x == 10:
        var = var - 10
    elif x == 5:
        var = var - 5

print("change owed: " + str(abs(var)))
