# this function removes spaces and new lines for column from right and left
def strip(string):
    return string.strip()

# this function reads database from contacts.txt file
def read_database():
    file = open("C:/Users/margu/Documents/GitHub/python-algajatele/11_test_of_input_output_arrays_conditionals/contacts.txt", encoding="utf-8")
    rows = []
    for row in file:
        rows.append(list(map(strip, row.split(", "))))
    return rows

# this function writes contacts to file
def write_database(db):
    file = open("C:/Users/margu/Documents/GitHub/python-algajatele/11_test_of_input_output_arrays_conditionals/contacts.txt", mode="w", encoding="utf-8")
    rows = []
    for row in db: 
        rows.append(", ".join(row))
    file.write("\n".join(rows))
    file.close()

# this function prints all contacts from db that is in memory
def print_out_database(db):
    print("Index \t Name \t\t Phone \t\t Age \t Email")
    for i in range(0, len(db)):
        row = db[i]
        print(i, "\t", row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t")

def print_out_commands():
    print("Commands are:")
    print("1. list users")
    print("2. edit user")
    print("3. add user")
    input("What is your command?: ")

def main():
  db = read_database()
  print_out_database(db)
  print_out_commands()


main()
