# functions

def add(inp):
    x = True
    while x == True:
            name = input("Enter name here: ")
            number = input("Enter phone number here: ")
            c = {"name": name, "phone #": number}
            contacts.append(c)
            n = input("Enter Y to add more and N to go back to menu: ")
            if n == "N":
                x = False
    return

def view(inp):
    x = True
    while x == True:
        for z in contacts:
            print(z)
        n = input("Enter Y to view again or N to go back to menu: ")
        if n == "N":
            x = False
    return

def search(inp):
    x = True
    while x == True:
        name = input("Enter name: ")
        for z in contacts:
            if z["name"] == name:
                found = True
                break
            else:
                found = False
        if found == True:
            print("Name: " + z["name"])
            print("Phone number" + z["phone #"])
        else:
            print("Name not found, please try again!")

        n = input("Enter Y to keep searching or N to go back to menu: ")
        if n == "N":
            x = False
    return

def remove(inp):
    x = True
    while x == True:
        name = input("Enter name: ")
        for z in contacts:
            if z["name"] == name:
                contacts.remove(z)
                print(name + " was removed from this list")

    n = input("Enter Y to remove again or N to go back to menu: ")
    if n == "N":
        x = False
    return

# program
contacts = []
loop = True
while loop == True:
    print("Contact book")
    print("Enter '1' to Add")
    print("Enter '2 to View")
    print("Enter '3' to Search")
    print("Enter '4' to Remove")
    print("Enter '0' to Exit")
    
    try:
        inp = int(input("Input here: "))
    except ValueError:
        print("Please enter a number!")
        continue
    
    if inp == 0 :
        loop = False
        
    elif inp == 1:
        add(inp)
    
    elif inp == 2:
        view(inp)

    elif inp == 3:
        search(inp)
    
    elif inp == 4:    
        remove(inp)
    else:
        print("Please enter a number between (0-4)")
