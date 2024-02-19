import re

def main():
    print(count(input("Text: ")))

def contador(um):
    i = 0
    for u in um:
        for x in u:
            match = re.search(r'^um(\.,)?[^a-z]|^um$',x.strip(),re.IGNORECASE)
            if match :
                i += 1
    return i

def count(s):
    um = re.findall(r'(^[um,.]+\s)|(\s[um,\.]+)|(^[um]+)',s,flags=re.IGNORECASE)
    return contador(um)

if __name__ == "__main__":
    main()