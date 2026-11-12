from books import *

#code for doing action

def main():
 while True:
    print("\n=======LIBRARY MANAGEMENT SYSTEM=======")
    print("1.Add new book")
    print("2. Display all book")
    print("3.Search a book")
    print("4.Student register")
    print("5.Issue a book")
    print("6.Return a book")
    print("7.Delete a book")
    print("8.exit")
    choice=input("enter your choice(from 1 to 8): ")
    if choice=="1":
        add_book()
    elif choice=="2":
        display_book()
    elif choice=="3":
         search_book()
    elif choice=="4":
        std_register()
    elif choice=="5":
        issue_book()
    elif choice=="6":
        back_book()
    elif choice=="7":
        delete()
    elif choice=="8":
        print("Thankyou so much for using")
        break
    else:
        print("invalid choice!")
main()