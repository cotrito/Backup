import requests
import sys
import json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#print(json.dumps(response.json(),indent = 2))
o = response.json()
val = o["bpi"]["USD"]["rate_float"]

try:
    n = float(sys.argv[1])
    res = '{:,.4f}'.format(n * float(val))
    print('$'+res)

except requests.RequestException:
    sys.exit("error")
except ValueError :
    sys.exit("error")

