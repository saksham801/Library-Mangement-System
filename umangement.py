from email.utils import encode_rfc2231

import pymongo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime,timedelta



def sending_bookdetail(email="", title = ""):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Book"]

    details =  collection.find_one({"Name":title})
    list1 = [details.get("Name"),
             details.get("Author"),
             details.get("Price"),
             details.get("Edition"),
             details.get("Genre"),
             details.get("Quantity"),
             details.get("Stock"),
             details.get("ISBN"),
             details.get("No of Pages"),
             details.get("Language")]

    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "USERNAME FROM LIBRARY MANAGEMENT SYSTEM [LMS]"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your Username HTML Content
    html = f"""
    <!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Book Details</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; background-color:#eef7f6; font-family:'Roboto', sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 40px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 6px 20px rgba(0,0,0,0.1);">
          <!-- Header -->
          <tr>
            <td style="background-color:#009688; padding: 30px 20px; text-align:center;">
              <h1 style="margin:0; font-size:26px; color:#ffffff;">Library Management System</h1>
              <p style="margin:6px 0 0; font-size:15px; color:#cdeae7;">Book Details</p>
            </td>
          </tr>
          <!-- Body -->
          <tr>
            <td style="padding: 35px 30px; color:#333;">
              <h2 style="margin-top:0; color:#009688;">Hello Reader,</h2>
              <p style="font-size:16px; line-height:1.6;">
                Here are the details of the book you're viewing:
              </p>
              <table width="100%" cellpadding="0" cellspacing="0" style="margin: 25px 0; font-size:16px;">
                <tr><td style="padding: 8px 0; color:#555;"><strong>Title:</strong></td><td style="padding: 8px 0; color:#000;">{title}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>Author:</strong></td><td style="padding: 8px 0; color:#000;">{list1[1]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>Price:</strong></td><td style="padding: 8px 0; color:#000;">{list1[2]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>Edition:</strong></td><td style="padding: 8px 0; color:#000;">{list1[3]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>Genre:</strong></td><td style="padding: 8px 0; color:#000;">{list1[4]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>Quantity:</strong></td><td style="padding: 8px 0; color:#000;">{list1[5]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>Availability:</strong></td><td style="padding: 8px 0; color:#000;">{list1[6]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>ISBN:</strong></td><td style="padding: 8px 0; color:#000;">{list1[7]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>No. of Pages:</strong></td><td style="padding: 8px 0; color:#000;">{list1[8]}</td></tr>
                <tr><td style="padding: 8px 0; color:#555;"><strong>Language:</strong></td><td style="padding: 8px 0; color:#000;">{list1[9]}</td></tr>
              </table>
              <p style="font-size:14px; color:#555; line-height:1.6;">
                Feel free to visit the library to reserve or issue this book. Availability is subject to change.
              </p>
              <br>
              <p style="font-size:14px; color:#009688;"><strong>- Library Management System Team</strong></p>
            </td>
          </tr>
          <!-- Footer -->
          <tr>
            <td style="background-color:#e0f2f1; text-align:center; padding: 18px; font-size:12px; color:#555;">
              © 2025 Library Management System. All rights reserved.
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>

    """

    # Attach HTML content
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f'''Details Send successfully to {email} If You don't recive it check your spam folder''')



    except Exception as e:
        print(f"Error sending email: {e}")


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


def reserved_book(email1 = ""):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Book"]
    collection2 = db["Reservation"]
    collection3 = db["User"]
    dict1 = {}

    title = input("Enter book title: ")
    if collection.find_one({"Name": title}):
        quantity = collection.find_one({"Name": title}).get("Quantity")
        if quantity <= 0:
            filter = {"Name": title}
            update = {"$set": {"Stock": "Out of Stock"}}
            collection.update_one(filter, update)
            print("So Sorry, Out of Stock")

        elif quantity >= 1:
            filter = {"Name": title}
            update = {"$set": {"Stock": "In Stock"}}
            collection.update_one(filter, update)
            book = collection.find_one({"Name": title})
            quant = {"Name": title}
            quant_filter = {"$set":{"Quantity":book["Quantity"]-1}}
            user_det = collection3.find_one({"email": email1})
            user_days = int(input("Enter number of days: "))
            from_date = datetime.now()
            to_date = from_date + timedelta(days=user_days)

            # Format dates
            from_str = from_date.strftime("%B %d, %Y")
            to_str = to_date.strftime("%B %d, %Y")

            dict1["Name"] = user_det.get("name")
            dict1["Title"] = title
            dict1["Author"] = book.get("Author")
            dict1["Email"] = user_det.get("email")
            dict1["Start Date"] = from_str
            dict1["End Date"] = to_str






            print("Successfully Resversed  book")
            collection.update_one(quant, quant_filter)
            collection2.insert_one(dict1)
            sending_res(email = email1)


    else:
        print("No book found")


def sending_res(email = ""):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Reservation"]

    det = collection.find_one({"Email": email})




    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "USERNAME FROM LIBRARY MANAGEMENT SYSTEM [LMS]"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your Username HTML Content
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Book Reservation Confirmation</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; background-color:#eef7f6; font-family:'Roboto', sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 40px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 6px 20px rgba(0,0,0,0.1);">
          <!-- Header -->
          <tr>
            <td style="background-color:#009688; padding: 30px 20px; text-align:center;">
              <h1 style="margin:0; font-size:26px; color:#ffffff;">Library Management System</h1>
              <p style="margin:6px 0 0; font-size:15px; color:#cdeae7;">Reservation Confirmed</p>
            </td>
          </tr>
          <!-- Body -->
          <tr>
            <td style="padding: 35px 30px; color:#333;">
              <h2 style="margin-top:0; color:#009688;">Hello Reader,</h2>
              <p style="font-size:16px; line-height:1.6;">
                Thank you for reserving a book. Below are your reservation details:
              </p>
              <table width="100%" cellpadding="0" cellspacing="0" style="margin: 25px 0; font-size:16px;">
                <tr>
                  <td style="padding: 8px 0; color:#555;"><strong>Book Title:</strong></td>
                  <td style="padding: 8px 0; color:#000;">{det.get("Title")}</td>
                </tr>
                <tr>
                  <td style="padding: 8px 0; color:#555;"><strong>Author:</strong></td>
                  <td style="padding: 8px 0; color:#000;">{det.get("Author")}</td>
                </tr>
                <tr>
                  <td style="padding: 8px 0; color:#555;"><strong>From Date:</strong></td>
                  <td style="padding: 8px 0; color:#000;">{det.get("Start Date")}</td>
                </tr>
                <tr>
                  <td style="padding: 8px 0; color:#555;"><strong>Due Date:</strong></td>
                  <td style="padding: 8px 0; color:#000;">{det.get("End Date")}</td>
                </tr>
              </table>
              <p style="font-size:14px; color:#555; line-height:1.6;">
                Kindly return or renew the book before the due date to avoid any late charges.
              </p>
              <br>
              <p style="font-size:14px; color:#009688;"><strong>- Library Management System Team</strong></p>
            </td>
          </tr>
          <!-- Footer -->
          <tr>
            <td style="background-color:#e0f2f1; text-align:center; padding: 18px; font-size:12px; color:#555;">
              © 2025 Library Management System. All rights reserved.
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>


    """

    # Attach HTML content
    part = MIMEText(html, "html")
    message.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f'''Details Send successfully to {email} If You don't recive it check your spam folder''')



    except Exception as e:
        print(f"Error sending email: {e}")





