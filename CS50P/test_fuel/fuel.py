import sys

def main():
   a = input("fuel level : ")
   print(gauge(convert(a)))

def convert(var):
   try :
         q = var.split("/")
         x = int(q[0])
         y = int(q[1])
         z = round((float(x) / float(y))*100)
         return z


   except EOFError:
      sys.exit()
   except ValueError :
      raise
   except ZeroDivisionError :
      raise
   except IndexError :
      pass
   except TypeError :
      pass

def gauge(z):

      if z > 98:
         return "F"
      elif z < 2:
         return "E"
      else :
         return f"{z}%"


if __name__ == "__main__":
    main()
