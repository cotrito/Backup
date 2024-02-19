def main():
   z = fuel()
   if z > 98:
      print("F")
   elif z < 2:
      print("E")
   else :
      print(f"{z}%")

def fuel():
      while True :
         try :
            var = input("fuel level : ")
            q = var.split("/")
            x = int(q[0])
            y = int(q[1])
            z = round((float(x) / float(y))*100)
            if z > 100 :
               pass
            else :
               return z

         except ValueError :
            pass
         except ZeroDivisionError :
            pass
         except IndexError :
            pass

main()