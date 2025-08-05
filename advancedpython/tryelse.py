try:
    a=int(input("enter the number"))
    print(a)

except Exception as e:
    print ("LAU LAU")
    print(e)
else: #only runs when try is successful
    print("I AM INSIDE ELSE")
