def divide (x,y):
    try:
        a = x/y
    except:
        print("ZeroDivisionError");
        f = open("stdout2.txt", 'a')
        print("0 input : ",x, y,  file=f)
        f.close() 
    else:
        return a