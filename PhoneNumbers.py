#function to print phone numbers
def print_numbers(numbers):
    print("Telphone Numbers:")
    for k,v in numbers.items():
        print("Name: ", k, "\tNumber: ", v)
    print()
#function to add phone numbers
def add_number(numbers,name,number):
    numbers[name] = number
#function to lookup phone numbers
def lookup_number(numbers,name):
    if name in numbers:
        return "The number is " + numbers[name]
    else:
        return name + " was not found"
'''
Example of how to use files
'''
#function to remove numbers
def remove_number(numbers,name):
    if name in numbers:
        del numbers[name]
    else:
        print(name," was not found")
#function to load numbers
def load_numbers(numbers,filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break;
        in_line = in_line[:-1]
        name,number = in_line.split(",")
        numbers[name] = number
    in_file.close()
#function to save numbers entered
def save_numbers(numbers,filename):
    out_file = open(filename,"wt")
    for k,v in numbers.items():
        out_file.write(k + "," + v + "\n")
    out_file.close()
#function to print menu options
def print_menu():
    print("1. Print Phone Number")
    print("2. Add a Phone Number")
    print("3. Remove a Phone Number")
    print("4. Lookup a Phone Number")
    print("5. Load numbers")
    print("6. Save numbers")
    print("7. Quit")
    print() #print blank line
#main
phone_list = {}
menu_choice = 0
print_menu()
while True:
    try:
        menu_choice = int(input("Type in a number (1-7): "))
        if menu_choice == 1:
            print_numbers(phone_list)
        elif menu_choice == 2:
            print("Add Name and Number")
            name = input("Name: ")
            phone = input("Number: ")
            add_number(phone_list, name, phone)
        elif menu_choice == 3:
            print("Remove Name and Number")
            name = input("Name: ")
            remove_number(phone_list, name)
        elif menu_choice == 4:
            print("Lookup Number")
            name = input("Name: ")
            print(lookup_number(phone_list, name))
        elif menu_choice == 5:
            filename = input("Filename to load: ")
            load_numbers(phone_list, filename)
        elif menu_choice == 6:
            filename = input("Filename to save: ")
            save_numbers(phone_list, filename)
        elif menu_choice == 7:
            break
        else:
            print_menu()
    except ValueError:
        print("You did not enter a number. Pleae try again...\n")
        print_menu()
    except FileNotFoundError:
        print("You did not enter the correct file/directory. Please try again...\n")
print("Goodbye")
