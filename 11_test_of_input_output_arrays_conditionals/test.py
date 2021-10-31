# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file
def read_database():
    file = open("contacts.txt", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file
def write_database(db):
    file = open("contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db: 
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory
def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    average = 0
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")
        average += int(row[2])
    print("Average age: ", average/len(db), "\n") #prints out average age of all users

def print_out_commands():
    print("Commands are:")
    print("1. list users")
    print("2. edit user")
    print("3. add user")
    print("4. remove user")
    print("\n")

def check_input():
    while(True):
        num = input("What is your command?: ")
        if (num == '1'):
            print_out_database(db)
            break
        elif (num == '2'):
            edit_user(db)
            break
        elif (num == '3'):
            add_user(db)
            break
        elif (num == '4'):
            remove_user(db)
            break
        else:
            print("Invalid input, please enter a number.")
            continue

def edit_user(db):
    while(True):     #making sure index entered is a number and is not out of range
        try:
            i = int(input("Enter index of user to edit: "))
            if(len(db) <= i or i < 0):
                print("Error out of index.")
                continue
            else:
                break
        except:
            print("Please enter a number.")
            continue
    
    user = db[i] #saving the selected row
    print(user, "\n")
    
    print("What would you like to change?")
    while(True): #checks if the chosen option is correct
        ci = input("Enter 'name', 'number', 'age' or 'email': ")
        if (ci != "name" and ci != "number" and ci != "age" and ci != "email"):
            print("Error, please choose one of the valid options.")
            continue
        else:
            break
    
    if (ci == 'name'):
        name = input("Enter new name: ")
        user[0] = name
    elif (ci == 'number'):
        number = input("Enter new number: ")
        user[1] = number
    elif (ci == 'age'):
        age = input("Enter new age: ")
        user[2] = age
    elif (ci == 'email'):
        mail = input("Enter new email: ")
        user[3] = mail
    
    db[i] = user
    write_database(db)
    print("Changed user successfully")

def add_user(db):
    row = []
    name = input("Enter name: ")
    phone = input("Enter phone number:")
    age = input("Enter age: ")
    email = input("Enter email: ")
    
    row.append(name)
    row.append(phone)
    row.append(age)
    row.append(email)
    
    db.append(row)
    write_database(db)
    print("Added user successfully")

def remove_user(db):
    while(True): #making sure index entered is a number and is not out of range
        try:
            i = int(input("Enter index of user to remove: "))
            if(len(db) <= i or i < 0):
                print("Error out of index.")
                continue
            else:
                break
        except:
            print("Please enter a number.")
            continue
    
    db.pop(i)
    write_database(db)
    print("Removed user successfully")

def main():
    while(True):
        print_out_commands()
        check_input()

db = read_database()
main()