# feisbuk.py (C) Aran Roig, 2020

def menu():
    print("=====================================")
    print("Welcome to Social Network")
    print("=====================================")
    print("new --> Create new user")
    print("cat --> Show user information")
    print("ls ---> List users")
    print("add --> Add friends to an user")
    print("se ---> Search user by pattern")
    print("mv ---> Modify user information")
    print("save ---> Save users to disk")
    print("load ---> Load users from disk")
    print("exit -> Logout")
    print("=====================================")
    return input("Enter option: ")

def newUser(userDict):
    print("=============================")
    print("Creating new user in Social Network")
    print("=============================")

    data = []

    dni = input("Enter dni: ")
    data.append(input("Enter name: "))
    data.append(input("Enter surname: "))
    data.append(input("Enter network: "))
    data.append(input("Enter town: "))
    data.append(input("Enter preference: "))
    data.append(input("Enter email: "))
    data.append(input("Enter password: "))

    data.append([])

    userDictionary[dni] = data

    print("User created")
    print("=============================")

    return userDictionary

def searchUser(userDictionary):
    print("=============================")
    print("Searching user in Social Network")
    print("=============================")
    dni = input("Enter dni: ")
    if not dni in userDictionary.keys():
        print("No user found")
    else:
        print("User found. Displaying information:")
        print("Name and surname: " + userDictionary[dni][0] + " " + userDictionary[dni][1])
        print("Network: " + userDictionary[dni][2])
        print("Town: " + userDictionary[dni][3])
        print("Preference: " + userDictionary[dni][4])
        print("Email: " + userDictionary[dni][5])

        print("=============================")

def listUsers(userDictionary):
    print("=============================")
    print("List users Social Network")
    print("=============================")

    i = 0
    for key in userDictionary:
        
        print("=============================")
        print("List users Social Network")
        print("=============================")
        
        print("Dni: " + key)
        print("Name and surname: " + userDictionary[key][0] + " " + userDictionary[key][1])
        print("Network: " + userDictionary[key][2])
        print("Town: " + userDictionary[key][3])
        print("Preference: " + userDictionary[key][4])
        print("Email: " + userDictionary[key][5])

        print("=============================")
        
        i += 1
    print(str(i) + " users found")

def acceptUser(userDictionary):
    print("=============================")
    print("Make friends in Social Network")
    print("=============================")
    dni1 = input("Enter dni1: ")
    dni2 = input("Enter dni2: ")

    if not dni1 in userDictionary.keys():
        print("dni1 is not user of Social Network")
        return userDictionary
    if not dni2 in userDictionary.keys():
        print("dni2 is not user of Social Network")
        return userDictionary
    print("dni1 and dni2 are users of Social Network")
    
    userDictionary[dni1][7].append(dni2)
    userDictionary[dni2][7].append(dni1)

    s = "Friends of " + str(dni1) + ":"
    for lel in userDictionary[dni1][7]:
        s += " " + str(lel)
    
    print(s)

    s = "Friends of " + str(dni2) + ":"
    for lel in userDictionary[dni2][7]:
        s += " " + str(lel)
    print(s)
    
    print("=============================")

    return userDictionary

def saveFile(userDict):
    
    f = open("data.txt", "w")
    for key in userDict:
        s = key + " "
        for i in range(0, 7):
            s += userDict[key][i] + " "
        for i in userDict[key][7]:
            s += i + " "
        s += '\n'
        f.write(s)
    f.close()
    
def readFile():
    userDictionary = {}
    try:
        with open("data.txt", "r") as f:
            for s in f.readlines():
                r = s.split()
                userDictionary[r[0]] = []
                userDictionary[r[0]].append(r[0])
                userDictionary[r[0]].append(r[1])
                userDictionary[r[0]].append(r[2])
                userDictionary[r[0]].append(r[3])
                userDictionary[r[0]].append(r[4])
                userDictionary[r[0]].append(r[5])
                userDictionary[r[0]].append(r[6])
                userDictionary[r[0]].append(r[7])
                userDictionary[r[0]].append([])                    
                if len(r) > 7:
                    for e in range(8, len(r)):
                        userDictionary[r[0]][8].append(r[e])
        return userDictionary
    except IOError:
        print("Problema")

def moveUser(userDict):
    print("=====================================")
    print("Modify User Information Social Network")
    print("=====================================")

    dni = input("Enter Dni: ")
    if dni in userDict:
        print("Existing user")
        passwd = input("Enter password for user " + str(dni) + ": ")
        if(userDict[dni][7] == passwd):
            print("Password correct")
            print("")
            print("Information for user " + str(dni) + ":")
            print("Name and surname: " + userDictionary[dni][0] + " " + userDictionary[dni][1])
            print("Network: " + userDictionary[dni][2])
            print("Town: " + userDictionary[dni][3])
            print("Preference: " + userDictionary[dni][4])
            print("Email: " + userDictionary[dni][5])
            print("=====================================")
            print("t. Modify town")
            print("p. Modify preference")
            print("e. Modify email")
            print("x. Exit")
            while True:
                option = input("Enter option:")
                print("")
                if option == "t":
                    town = input("Enter new town: ")
                    userDict[dni][3] = town
                    print("Changes done")
                elif option == "p":
                    town = input("Enter new preference: ")
                    userDict[dni][4] = town
                    print("Changes done")
                elif option == "e":
                    town = input("Enter new email: ")
                    userDict[dni][5] = town
                    print("Changes done")
                elif option == "x":
                    return userDict
        else:
            return userDict
    else:
        print("User doesn't exist")
        return userDict

def searchPattern(userDictionary):
    print("=====================================")
    print("Search Social Network users")
    print("=====================================")
    pattern = input("Enter pattern to search: ")

    subuserDictionary = {}
    for key in userDictionary:
        for i in userDictionary[key][:7]:
            if i == pattern:
                subuserDictionary[key] = userDictionary[key]
    if len(userDictionary) == 0:
        print("0 users found in Social Network")
    else:
        for key in subuserDictionary:
            print("")
            print("Name and surname: " + userDictionary[key][0] + " " + userDictionary[key][1])
            print("Network: " + userDictionary[key][2])
            print("Town: " + userDictionary[key][3])
            print("Preference: " + userDictionary[key][4])
            print("Email: " + userDictionary[key][5])
            print("Friends:")
            for friend in subuserDictionary[key][7]:
                print(friend)
            print("")        
        print(str(len(subuserDictionary)) + " matching users with pattern " + pattern + " in Social Network")

validOptions = ["new", "cat", "ls", "add", "se", "mv", "save", "load"]
userDictionary = {}

while True:
    cin = menu()
    if cin == "exit":
        break
    if cin in validOptions:
        if cin == "new":
            userDictionary = newUser(userDictionary)
        elif cin == "cat":
            searchUser(userDictionary)
        elif cin == "ls":
            listUsers(userDictionary)
        elif cin == "add":
            userDictionary = acceptUser(userDictionary)
        elif cin == "se":
            searchPattern(userDictionary)
        elif cin == "mv":
            userDictionary = moveUser(userDictionary)
        elif cin == "save":
            saveFile(userDictionary)
        elif cin == "load":
            userDictionary = readFile()
        else:
            print("Watafak")
    else:
        print ("Error, please select a valid option in the list below")