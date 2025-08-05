try:
    a=int(input("enter the number"))
    print(a)
except Exception as e:
    print ("LAU LAU")
    print(e)
except ValueError as v:
    print ("LAU LAU")
    print(v)
