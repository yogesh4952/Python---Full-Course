prompt  = input("> ").lower();
while(prompt !="quit"):

    if prompt=='help':
        print("""

    start - to start the car
    stop - to stop the car
    quit - to exit
    """)
    elif prompt == 'start':
        print("Car started!")
    elif prompt =='stop':
        print("Car stopped")
    elif prompt =="quit":
        print("quited")
    else:
        print("I don't understand that..")
    prompt  = input("> ").lower()
    

