def main_menu():
    while True:
        print("\nNordstern Helpdesk Tool")
        print("=======================")
        print("1. Show system snapshot")
        print("2. Check user list")
        print("3. Show ticket overview")
        print("4. Analyze tickets by priority and status")
        print("5. Show critical open tickets")
        print("6. Analyze log file")
        print("7. Create support report")
        print("8. Exit program")

        choice = input("Choose an option: ")

        if choice == "1":
            print("System snapshot will be shown here.")
        elif choice == "2":
            print("User list validation will be shown here.")
        elif choice == "3":
            print("Ticket overview will be shown here.")
        elif choice == "4":
            print("Ticket analysis will be shown here.")
        elif choice == "5":
            print("Critical open tickets will be shown here.")
        elif choice == "6":
            print("Log analysis will be shown here.")
        elif choice == "7":
            print("Support report will be created here.")
        elif choice == "8":
            print("Program ended.")
            break
        else:
            print("Invalid input. Please choose a number from 1 to 8.")


main_menu()