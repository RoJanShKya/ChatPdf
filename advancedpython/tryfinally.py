def main():
    try:
        a=int(input("enter the number"))
        print(a)

    except Exception as e:
        print ("LAU LAU")
        print(e)
        
    finally: #always runs
        print("I AM INSIDE FINALLY")
main()