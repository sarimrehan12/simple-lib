book_list =list
menu= '''
1) Add book
2) Remove book
3) View book
4) Press E to exit
'''
def add_book(booklist, book):
    booklist.append(book)
    print("Book added successfully")

def remove_book(booklist, book):
    if book in booklist:
        booklist.remove(book)
        print("Book removed sucessfully")
    else:
        print("Book was not found in the list")

def display_list (booklist):
    if booklist:
        print("Added books ->",",".join (booklist))
    else:
        print("No books in the list")

def exit_program():
    print("Thank you for visiting book library system")
    quit()

while True:
    print(menu)
    choice = input("Your choice:")

    if choice == "1":
        book_name = input("Enter th book name:")
        add_book(book_list, book_name)

    elif choice == "2":
       book_name = input ("Enter the book name to remove:")
       remove_book(book_list, book_name)

    elif choice == "3":
        display_list(book_list)
    elif choice.lower()== "e":
        exit_program()
    else :
        print("Invalid entry")
        input("please enter to return to main value")
