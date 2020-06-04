# feisbuk.py (C) Aran Roig, 2020

def menu():
    option = "SASass"
    while(option != "exit"):
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
        option = input("Enter option:")

userDictionary = {}

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
        for i in range(0, 6):
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
                print(len(r))
                userDictionary[r[0]] = []
                userDictionary[r[0]].append(r[0])
                userDictionary[r[0]].append(r[1])
                userDictionary[r[0]].append(r[2])
                userDictionary[r[0]].append(r[3])
                userDictionary[r[0]].append(r[4])
                userDictionary[r[0]].append(r[5])
                userDictionary[r[0]].append([])                    
                if len(r) > 6:
                    for e in range(6, len(r)-1):
                        print("Wat")
                        userDictionary[r[0]][6].append(r[e])
        return userDictionary
    except IOError:
        print("Problema")

userDictionary = newUser(userDictionary)
userDictionary = newUser(userDictionary)
userDictionary = acceptUser(userDictionary)
print(userDictionary)
saveFile(userDictionary)
print(readFile())