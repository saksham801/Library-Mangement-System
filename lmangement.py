import pymongo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime,timedelta

def issued_book():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["Reservation"]

    details = collection.find({})
    for doc in details:
        for key, value in doc.items():
            if key !=  "_id":
                print(f"{key} : {value}")
        print()


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
             details.get("No of page"),
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


def user_details():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["User"]

    user_email = input("Enter user email: ")
    if collection.find_one({"email": user_email}):
        details = collection.find_one({"email": user_email})
        for key, value in details.items():
            if key != "_id":
                if key != "password":
                    print(f"{key} : {value}")
        print()

    else:
        print("No user found")


