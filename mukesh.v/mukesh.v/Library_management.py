details=[]
while True:
    choice=int(input('choose the following menu: \n 1.ADD Book. \n 2.Search Book. \n 3.Issue Book. \n 4.Return Book. \n 5.Update Book. \n 6.Delete Book. \n 7.Display All Books. \n 8.Sort book by price. \n 9.Exit\n'))
    match choice:
        case 1:
            def add_book():
                book_id=int(input("enter the book id:"))
                name=input("enter the book name:").upper()
                author_name=input("enter the name of the auther for the book:").upper
                category=input("enter the category of the book:")
                price=float(input("enter the price of the book:"))
                quantity = int(input("enter the quantity of the book:"))
                details.append({
                    'id':book_id,
                    "name":name,
                    "author":author_name,
                    "category":category,
                    "price":price,
                    "quantity":quantity
                })
                print(details)
            add_book()
        case 2:
            def search_book():
                 search_id= int(input("please enter the id of the book you want to search for ")) 
                 for book in details :
                     if book['id'] == search_id:
                         print ('here is the employee you searched for:') 
                         print(f'book found: Name: {book["name"]}, ID: {book["id"]}, author: {book["author"]}, price: {book["price"]}') 
                         break 
                     else:
                         print('Employee not found')

            search_book()
        case 3:
            def issue_book():
                issue_id=int(input("enter the input of the book:"))
                for i in details:
                    if i["id"]==issue_id:
                        i["quantity"]-=1
                        print("book issued successfully")
                    else:
                        print("not")
            issue_book()
        
        case 4:
            def return_book():
                return_id=int(input("enter the input of the book:"))
                for i in details:
                    if i["id"]==return_id:
                        i["quantity"]+=1
                        print("book returned")
            return_book()
        case 5:
            def update_book():
                update_id = int(input("Enter the Book ID to update: "))

                for book in details:
                    if book["id"] == update_id:
                        print("\nBook Found!")
                        print(book)

                        book["name"] = input("Enter new Book Name: ")
                        book["author"] = input("Enter new Author Name: ")
                        book["category"] = input("Enter new Category: ")
                        book["price"] = float(input("Enter new Price: "))
                        book["quantity"] = int(input("Enter new Quantity: "))
                        
                    
                    

                        print("\nBook Updated Successfully!")
                        print(book)
                        break
                else:
                    print("Book not found!")

            update_book()
        case 6:
            def delete_book():
                delete_id = int(input("Enter the Book ID to delete: "))

                for book in details:
                    if book["id"] == delete_id:
                        details.remove(book)
                        print("Book deleted successfully!")
                        break
                else:
                    print("Book not found!")

            delete_book()
                            
        case 7:
            def display_books():
                if len(details) == 0:
                    print("No books available in the library.")
                else:
                    
                    for book in details:
                        print(f"""
                        Book ID   : {book['id']}
                        Book Name : {book['name']}
                        Author    : {book['author']}
                        Category  : {book['category']}
                        Price     : ${book['price']}
                        Quantity  : {book['quantity']}""")

            display_books()
        case 8:
            def sort_book():
                if len(details) == 0:
                    print("No books available to sort.")
                else:
                    sorted_books = sorted(details,key=lambda X:X < 'price',reverse=True)

                    for book in sorted_books:
                        print(f"""
                        Book ID   : {book['id']}
                        Book Name : {book['name']}
                        Author    : {book['author']}
                        Category  : {book['category']}
                        Price     : ${book['price']}
                        Quantity  : {book['quantity']}""")

            sort_book()
        case 9:
            print("exitted successfully")
            break

discount= lambda price:price-price*(10/100)       
print ('discount=',discount)