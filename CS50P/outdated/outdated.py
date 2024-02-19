def main():

    print(dt_tran())

def dt_tran():
    while True :
        try :
            val = input("Date : ")
            val2 = val.strip()
            x = val2.split('/')
            if int(x[1]) <1 or int(x[1])>31 :
                pass
            elif len(x[1]) == 1:
                d = "0"+str(x[1])
            elif len(x[1]) == 2:
                d = str(x[1])
            else :
                pass
            if int(x[0]) < 1 or int(x[0]) > 12:
                pass
            elif len(x[0]) == 1:
                m = "0"+str(x[0])
            elif len(x[0]) == 2:
                m = str(x[0])
            else :
                pass
            if len(x[2]) :
                a = x[2]
            else :
                pass
            ft = str(a) +"-"+ m +"-"+ d
            return ft
        except UnboundLocalError:
            pass
        except ValueError:
            pass
        except IndexError:
            try :
                dt =["January","February","March","April","May","June","July","August","September","October","November","December"]
                i = 1
                dict_dt = {}
                for s in dt :
                    if len(str(i)) == 1:
                        dict_dt[s] = "0"+str(i)
                    else :
                        dict_dt[s] = str(i)
                    i +=1
                if val.find(',') == -1:
                    val =[]
                else:
                    pass
                y = val.split(' ')
                m = dict_dt[y[0]]
                val_d = y[1].replace(',','')
                if int(val_d) <1 or int(val_d)>31:
                    pass
                elif len(val_d) == 1:
                    d = "0"+val_d
                elif  len(val_d) == 2:
                    d = val_d
                else :
                    pass
                if len(y[2]) == 4:
                    a = y[2]
                else:
                    pass
                fin = a + "-" + m +"-"+ d
                return fin

            except UnboundLocalError:
                pass
            except IndexError:
                pass
            except KeyError:
                pass
            except AttributeError:
                pass

main()