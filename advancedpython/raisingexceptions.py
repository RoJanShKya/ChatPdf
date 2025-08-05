a=int(input("enter the first number"))
b=int(input("enter the second number"))
if(b==0):
    raise ZeroDivisionError("DONT DIVIDE BY ZERO")
else:
    print (f"DIVISION IS {a/b}")