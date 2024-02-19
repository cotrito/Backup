import re

def main():
    print(convert(input("Hours: ")))

def valid_time(ft):
    if ':' in ft:
        ft_h, ft_m = ft.split(':')
        if int(ft_h) <=12 and int(ft_m) <60 :
            return True
        else :
            return False
    else :
        if int(ft) <=12:
            return True
        else :
            return False

def convert_time(ft,fm):
    if ':' in ft and fm.strip().upper() == 'PM':
        ft_h, ft_m = ft.split(':')
        if int(ft_h) == 12:
            return f'{int(ft_h)}:{ft_m}'
        else :
            return f'{int(ft_h)+12}:{ft_m}'
    if ':' in ft and fm.strip().upper() == 'AM':
        ft_h, ft_m = ft.split(':')
        if int(ft_h) <10:
            return f'0{int(ft_h)}:{ft_m}'
        elif int(ft_h) == 12:
            return f'00:{ft_m}'
        else :
            return f'{int(ft_h)}:{ft_m}'
    elif ':' not in ft and fm.strip().upper() == 'PM':
        if int(ft) == 12:
            return f'{int(ft)}:00'
        else :
            return f'{int(ft)+12}:00'
    elif ':' not in ft and fm.strip().upper() == 'AM':
        if int(ft) <10 :
            return f'0{ft}:00'
        elif int(ft) == 12:
            return f'00:00'
        else :
            return f'{ft}:00'
    else :
        return ft

def convert(s):
    mach = re.search(r'([0-9:]+)\s([amp]{2}\s)?to\s([0-9:]+)\s([amp]{2})?',s,re.IGNORECASE)
    if mach :
        ft,fm,st,sm = mach.groups()
        if valid_time(ft) == True and valid_time(st) == True:
            pri = convert_time(ft.strip(),fm.strip())
            sec = convert_time(st.strip(),sm.strip())
            return pri+" to "+sec
        else :
            raise ValueError
    else :
        raise ValueError

if __name__ == "__main__":
    main()