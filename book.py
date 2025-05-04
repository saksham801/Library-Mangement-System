import pymongo



def new_book():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Book"]
    dict1 = {}

    name = input("Enter book name: ")
    dict1["Name"] = name

    author = input("Enter book author: ")
    dict1["Author"] = author

    price = input("Enter book price: ")
    dict1["Price"] = "₹" + price

    edition = input("Enter book edition: ")
    dict1["Edition"] = edition

    genre = input("Enter book genre: ")
    dict1["Genre"] = genre

    quantity = int(input("Enter book quantity: "))
    dict1["Quantity"] = quantity

    if quantity <= 0:
        avail = "Out of Stock"
        dict1["Availability"] = avail
    else:
        avail = "In Stock"
        dict1["Availability"] = avail

    isbn = input("Enter book ISBN: ")
    dict1["ISBN"] = isbn

    no_of_pages = int(input("Enter book no of pages: "))
    dict1["No of Pages"] = no_of_pages

    language = input("Enter book language: ")
    dict1["Language"] = language

    collection.insert_one(dict1)


def find_book():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Book"]

    print('''1. Name
2. Author
3. Price
4. Edition
5. Genre
6. Quantity
7. Availability
8. ISBN
9. No of Pages
10. Language
11. Quantity''')

    user_choice = int(input("Enter your choice (default 1) : "))
    if user_choice == 1 or user_choice == "" or user_choice is None:
        name = input("Enter book name: ")
        if collection.find_one({"Name": name}):
            book_details = collection.find_one({"Name": name})
            for key, value in book_details.items():
                if key != "_id":
                    print(f"{key} : {value}")

            print()




        else:

            print("No book found")

    elif user_choice == 2:
        author = input("Enter book author: ")

        book_details1 = collection.find({"Author": author})
        for doc in book_details1:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 3:
        price = input("Enter book price: ")

        book_details2 = collection.find({"Price": price})
        for doc in book_details2:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 4:
        edition = input("Enter book edition: ")
        book_details3 = collection.find({"Edition": edition})
        for doc in book_details3:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 5:
        genre = input("Enter book genre: ")
        book_details4 = collection.find({"Genre": genre})
        for doc in book_details4:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 6:
        quantity = input("Enter book quantity: ")
        book_details5 = collection.find({"Quantity": quantity})
        for doc in book_details5:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 7:
        avail = input("Enter book availability: ")
        book_details6 = collection.find({"Availability": avail})
        for doc in book_details6:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 8:
        isbn = input("Enter book ISBN: ")
        book_details7 = collection.find({"ISBN": isbn})
        for doc in book_details7:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 9:
        no_of_pages = input("Enter book no of pages: ")
        book_details8 = collection.find({"No of Pages": no_of_pages})
        for doc in book_details8:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 10:
        language = input("Enter book language: ")
        book_details9 = collection.find({"Language": language})
        for doc in book_details9:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    elif user_choice == 11:
        quantity = input("Enter book quantity: ")
        book_details10 = collection.find({"Quantity": quantity})
        for doc in book_details10:
            for key, value in doc.items():
                if key != "_id":
                    print(f"{key} : {value}")
        print()

    else:
        print("Invalid choice")


def update_book():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Book"]

    print('''1.Price
2. Language
3. Quantity
4. Edition''')

    user_choice = int(input("Enter your choice (default 1) : "))
    if user_choice == 1:
        name = input("Enter book name: ")
        details = collection.find_one({"Name": name})
        old_price = details.get("Price")
        filter = {"Price": old_price}
        new_price = input("Enter new price: ")
        new_price1 = "₹"+new_price
        update = {"$set": {"Price": new_price1}}
        collection.update_one(filter, update)

    elif user_choice == 2:
        name = input("Enter book name: ")
        details = collection.find_one({"Name": name})
        old_language = details.get("Language")
        filter = {"Language": old_language}
        new_language = input("Enter new language: ")
        update = {"$set": {"Language": new_language}}
        collection.update_one(filter, update)

    elif user_choice == 3:
        name = input("Enter book name: ")
        details = collection.find_one({"Name": name})
        old_quantity = details.get("Quantity")
        filter = {"Quantity": old_quantity}
        new_quantity = int(input("Enter new quantity: "))
        update = {"$set": {"Quantity": new_quantity}}
        collection.update_one(filter, update)

    elif user_choice == 4:
        name = input("Enter book name: ")
        details = collection.find_one({"Name": name})
        old_edition = details.get("Edition")
        filter = {"Edition": old_edition}
        new_edition = input("Enter new edition: ")
        update = {"$set": {"Edition": new_edition}}
        collection.update_one(filter, update)

    else:
        print("Invalid choice")


def delete_book():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Book"]

    title = input("Enter book title: ")
    details = collection.find_one({"Title": title})
    if details:
        collection.delete_one({"Title": title})
        print("Delete successfully")
    else:
        print("Book not found")
