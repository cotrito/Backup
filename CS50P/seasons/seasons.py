from datetime import date, datetime
import sys
import inflect

def main():
   print(calculate_minuts(input("time of birth: ")))
   #print(calculate_minuts('1988-06-24'))

def calculate_minuts(s):
    p = inflect.engine()
    try :
        hoy = date.today()
        hoy = datetime.fromisoformat(str(hoy))
        fec_nac = datetime.fromisoformat(s)
        delta = hoy - fec_nac
        minutes = int((delta.total_seconds())/60)
        resultado = p.number_to_words(minutes).capitalize().replace('and ','')
        return f'{resultado} minutes'

    except ValueError:

        sys.exit("invalid date format")

if __name__ == "__main__":
    main()