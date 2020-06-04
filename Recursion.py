print("Will learn Resursion")

def greet():
    print("Hiiii")
    # Calling function itself and it goes on looping infinite times
    # limit of resursion is 1000 times so it will call 993 times only
    greet()

greet()
