class Library:
    def __init__(self,list,name):
        self.listofbooks = list
        self.library_name = name
        self.lendDict = {}
    def display_books(self):
        print("All books are Here.....:")
        for book in self.listofbooks:
            print(book)

    def lend_book(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lander-book DataBase has been updated. You can take book now ")
        else:
            print(f'Book is already being used by {self.lendDict[book]}')

    def add_book(self,book):
        import time
        self.listofbooks.append(book)
        print("Book is adding.")
        time.sleep(1)
        print(".",end='')
        time.sleep(1)
        print(".", end='')
        time.sleep(1)
        print(".", end='')
        print("Book has been added successfully")
    def return_book(self,book):
        self.lendDict.pop(book)
    def deleteBook(self,book):
        import time
        print("Book deleting")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".", end="")
        time.sleep(1)
        print(".",end="")
        self.listofbooks.remove(book)
        print(f"Book deleted successfully")


if __name__ == '__main__':
    avii=Library(['Python', 'Rich dady poor dady', 'Game of Thrones','Chacha Chodhary', 'Math', 'English', 'Science', 'Physics', 'Chemistry', 'The story of my life', 'HTML & CSS', 'Harry Potter', 'BatMan', 'Hacking'], 'Abhishek')
    secretkey=98765


    while(True):
        import time
        print(f"Welcome to the {avii.library_name} library. Enter your choice to continue:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Delete Book")
        choice = input()
        if choice not in ['1', '2', '3', '4', '5']:
            time.sleep(1)
            print("!", end='')
            time.sleep(1)
            print("!", end='')
            time.sleep(1)
            print("!!")
            print("[Error:0]Please enter a valid option")
            time.sleep(2)

            continue

        else:
            choice = int(choice)

        if choice == 1:
            avii.display_books()

        elif choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            avii.lend_book(user, book)

        elif choice == 3:
            book = input("Enter the name of the book you want to add: ")
            avii.add_book(book)

        elif choice == 4:
            book = input("Enter the name of the book you want to return: ")
            avii.return_book(book)

        elif choice == 5:
            book = input("Enter the name of the book you want to delete: ")
            if book in avii.listofbooks:
                key=int(input('Enter the password: '))
                if key == secretkey:
                    avii.deleteBook(book)
                else:
                    print("[Error:0] You enter the wrong password")
                    print("Please Enter the valid password")
            else:
                print("The book is not present in this library!",end='')
                time.sleep(1)
                print("!",end='')
                time.sleep(1)
                print("!", end='')
                time.sleep(1)
                print("!")
                time.sleep(1)
                continue

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue:")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                print("Have a Good Day Sir..")
                exit()

            elif user_choice2 == "c":
                continue
