import pymongo
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pyttsx3
import string
import os
import requests
from datetime import datetime
import umangement as um


def ip():
    # Get public IP address and location info
    response = requests.get("https://ipinfo.io/json")

    if response.status_code == 200:
        data = response.json()
        ip_address = data.get("ip")
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        location = f"{city}, {region}, {country}"

        return ip_address, location
    else:
        print("Failed to retrieve IP information.")


def generate_otp(length=6):
    """Generate an alphanumeric OTP with uppercase letters and digits."""
    characters = string.ascii_uppercase + string.digits
    otp = ''.join(random.choices(characters, k=length))
    return otp


def sending_otp(otp=generate_otp(6), email=''):
    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "OTP FROM LIBRARY MANAGEMENT SYSTEM [LMS]"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your OTP HTML Content
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Your OTP Code</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; font-family: 'Roboto', sans-serif; background-color:#f4f4f4;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f4; padding: 30px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1);">
          <!-- Header -->
          <tr>
            <td style="background-color:#004080; padding: 20px; color:#ffffff; text-align:center;">
              <h1 style="margin:0; font-size:24px;">Library Management System</h1>
              <p style="margin:0; font-size:14px;">Secure OTP Verification</p>
            </td>
          </tr>

          <!-- Body Content -->
          <tr>
            <td style="padding: 30px; color:#333333;">
              <h2 style="color:#004080;">Hello Reader,</h2>
              <p style="font-size:16px;">You're trying to access your account from the Library Management System.</p>
              <p style="font-size:16px;">Please use the following OTP to verify your identity:</p>

              <div style="margin: 30px 0; text-align: center;">
                <span style="display:inline-block; background-color:#004080; color:#ffffff; padding:15px 30px; font-size:24px; font-weight:bold; letter-spacing:5px; border-radius:8px;">
                  {otp}
                </span>
              </div>

              <p style="font-size:14px; color:#555;">This OTP is valid for only 10 minutes. Do not share it with anyone.</p>
              <p style="font-size:14px; color:#999;">If you did not request this OTP, please ignore this email.</p>
              <br>
              <p style="font-size:14px; color:#004080;">– Library Management System</p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color:#eeeeee; padding: 15px; text-align:center; font-size:12px; color:#888;">
              &copy; 2025 Library Management System. All rights reserved.
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
        print(f'''OTP Send successfully to {email} If You don't recive it check your spam folder''')

        user = input("Enter Your OTP Code: ")
        if user == otp:
            print("OTP Successfully Verified")
            return True
        else:
            print("OTP Failed")
            return False

    except Exception as e:
        print(f"Error sending email: {e}")


def sending_username(email="", username=""):
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
  <title>Your Username</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; font-family: 'Roboto', sans-serif; background-color:#f4f4f4;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f4; padding: 30px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1);">
          
          <!-- Header -->
          <tr>
            <td style="background-color:#004080; padding: 20px; color:#ffffff; text-align:center;">
              <h1 style="margin:0; font-size:24px;">Library Management System</h1>
              <p style="margin:0; font-size:14px;">Your Login Information</p>
            </td>
          </tr>

          <!-- Body Content -->
          <tr>
            <td style="padding: 30px; color:#333333;">
              <h2 style="color:#004080;">Hello Reader,</h2>
              <p style="font-size:16px;">Thank you for registering with the Library Management System.</p>
              <p style="font-size:16px;">Here is your username:</p>

              <div style="margin: 30px 0; text-align: center;">
                <span style="display:inline-block; background-color:#004080; color:#ffffff; padding:15px 30px; font-size:24px; font-weight:bold; border-radius:8px;">
                  {username}
                </span>
              </div>

              <p style="font-size:14px; color:#555;">Please keep this username safe. You will need it to log in to your account.</p>
              <p style="font-size:14px; color:#999;">If you did not create this account, you can ignore this email.</p>
              <br>
              <p style="font-size:14px; color:#004080;">– Library Management System</p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color:#eeeeee; padding: 15px; text-align:center; font-size:12px; color:#888;">
              &copy; 2025 Library Management System. All rights reserved.
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
        print(f'''Username Send successfully to {email} If You don't recive it check your spam folder''')



    except Exception as e:
        print(f"Error sending email: {e}")


def sending_password(email="", password1=""):
    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = " PASSWORD FROM LIBRARY MANAGEMENT SYSTEM [LMS]"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your Username HTML Content
    html = f"""
    <!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Your Username</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; font-family: 'Roboto', sans-serif; background-color:#f4f4f4;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f4; padding: 30px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:10px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.1);">
          
          <!-- Header -->
          <tr>
            <td style="background-color:#004080; padding: 20px; color:#ffffff; text-align:center;">
              <h1 style="margin:0; font-size:24px;">Library Management System</h1>
              <p style="margin:0; font-size:14px;">Your Login Information</p>
            </td>
          </tr>

          <!-- Body Content -->
          <tr>
            <td style="padding: 30px; color:#333333;">
              <h2 style="color:#004080;">Hello Reader,</h2>
              <p style="font-size:16px;">Thank you for registering with the Library Management System.</p>
              <p style="font-size:16px;">Here is your password:</p>

              <div style="margin: 30px 0; text-align: center;">
                <span style="display:inline-block; background-color:#004080; color:#ffffff; padding:15px 30px; font-size:24px; font-weight:bold; border-radius:8px;">
                  {password1}
                </span>
              </div>

              <p style="font-size:14px; color:#555;">Please keep this username safe. You will need it to log in to your account.</p>
              <p style="font-size:14px; color:#999;">If you did not create this account, you can ignore this email.</p>
              <br>
              <p style="font-size:14px; color:#004080;">– Library Management System</p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color:#eeeeee; padding: 15px; text-align:center; font-size:12px; color:#888;">
              &copy; 2025 Library Management System. All rights reserved.
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
        print(f'''Password Send successfully to {email} If You don't recive it check your spam folder''')

    except Exception as e:
        print(f"Error sending email: {e}")


def sending_greeting(email=""):
    # Email details
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Greeting From LIBRARY MANAGEMENT SYSTEM [LMS] "
    message["From"] = sender_email
    message["To"] = receiver_email

    # Your Username HTML Content
    html = f"""
    <!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Welcome to the Library</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; font-family: 'Roboto', sans-serif; background-color:#e8f0fe;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 30px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 6px 18px rgba(0,0,0,0.1);">
          <tr>
            <td style="background-color:#0097a7; padding: 25px; text-align:center;">
              <h1 style="margin:0; font-size:26px; color:#ffffff;">Library Management System</h1>
              <p style="margin:5px 0 0; font-size:15px; color:#e0f7fa;">Welcome Aboard!</p>
            </td>
          </tr>
          <tr>
            <td style="padding: 30px; color:#333;">
              <h2 style="color:#00796b;">Hello Reader,</h2>
              <p style="font-size:16px;">Thank you for registering with our Library Management System!</p>
              <p style="font-size:16px;">You now have access to thousands of books, resources, and library services at your fingertips.</p>
              <div style="margin: 30px 0; text-align: center;">
                <span style="display:inline-block; background-color:#00796b; color:#ffffff; padding:15px 25px; font-size:18px; font-weight:bold; border-radius:10px;">
                  Happy Reading!
                </span>
              </div>
              <p style="font-size:14px; color:#555;">If you have any questions, feel free to reach out to our support team anytime.</p>
              <br>
              <p style="font-size:14px; color:#00796b;">- Library Management System Team</p>
            </td>
          </tr>
          <tr>
            <td style="background-color:#f1f1f1; text-align:center; padding: 15px; font-size:12px; color:#666;">
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
        print(f'''Greeting Send successfully to {email} If You don't recive it check your spam folder''')

    except Exception as e:
        print(f"Error sending email: {e}")


def sending_login(email=""):
    sender_email = "dubeysaksham796@gmail.com"
    receiver_email = email
    password = "dfnfoasnifvnhzwt"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Greeting From LIBRARY MANAGEMENT SYSTEM [LMS] "
    message["From"] = sender_email
    message["To"] = receiver_email

    now = datetime.now()
    date = now.strftime("%B %d, %Y")
    time1 = now.strftime("%I:%M %p")

    ip_add, location = ip()

    # Your Username HTML Content
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Login Notification</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  </style>
</head>
<body style="margin:0; padding:0; font-family: 'Roboto', sans-serif; background-color:#e8f0fe;">
  <table width="100%" cellpadding="0" cellspacing="0" style="padding: 30px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; border-radius:12px; overflow:hidden; box-shadow:0 6px 18px rgba(0,0,0,0.1);">
          <tr>
            <td style="background-color:#0097a7; padding: 25px; text-align:center;">
              <h1 style="margin:0; font-size:26px; color:#ffffff;">Library Management System</h1>
              <p style="margin:5px 0 0; font-size:15px; color:#e0f7fa;">Login Alert</p>
            </td>
          </tr>
          <tr>
            <td style="padding: 30px; color:#333;">
              <h2 style="color:#00796b;">Hello Reader,</h2>
              <p style="font-size:16px;">We noticed a new login to your account on the Library Management System.</p>
              
              <table width="100%" cellpadding="0" cellspacing="0" style="margin: 20px 0; font-size:16px;">
                <tr>
                  <td style="padding: 10px 0; color:#555;"><strong>Date:</strong></td>
                  <td style="padding: 10px 0; color:#333;">{date}</td>
                </tr>
                <tr>
                  <td style="padding: 10px 0; color:#555;"><strong>Time:</strong></td>
                  <td style="padding: 10px 0; color:#333;">{time1} (IST)</td>
                </tr>
                <tr>
                  <td style="padding: 10px 0; color:#555;"><strong>IP Address: </strong></td>
                  <td style="padding: 10px 0; color:#333;"> {" "+ip_add}</td>
                </tr>
                <tr>
                  <td style="padding: 10px 0; color:#555;"><strong>Location:</strong></td>
                  <td style="padding: 10px 0; color:#333;"> {location}</td>
                </tr>
              </table>

              <p style="font-size:14px; color:#555;">If this was you, no further action is required.</p>
              <p style="font-size:14px; color:#d32f2f;">If you did not login, please reset your password immediately and contact our support team.</p>
              <br>
              <p style="font-size:14px; color:#00796b;">- Library Management System Team</p>
            </td>
          </tr>
          <tr>
            <td style="background-color:#f1f1f1; text-align:center; padding: 15px; font-size:12px; color:#666;">
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
        print(f'''Login Details Send successfully to {email} If You don't recive it check your spam folder''')

    except Exception as e:
        print(f"Error sending email: {e}")


def register():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["User"]
    dict1 = {}

    try:

        name = input("Enter your name: ")
        dict1["name"] = name

        surname = input("Enter your surname: ")
        dict1["surname"] = surname

        age = int(input("Enter your age: "))
        dict1["age"] = age

        phone = int(input("Enter your phone number: "))
        dict1["phone"] = phone

        email1 = input("Enter your email: ")

        if collection.find_one({"email": email1}):
            print("Email Already Exists")
        else:
            if sending_otp(email=email1) == True:
                dict1["email"] = email1

                username = input("Enter your username: ")
                dict1["username"] = username

                password = input("Enter your password: ")
                dict1["password"] = password

                collection.insert_one(dict1)
                sending_greeting(email=email1)
                return True

            else:
                print("Invalid OTP")
                return False

    except Exception as e:
        print(f"Error occurced: {e}")
        return False


def login():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["User"]
    text = pyttsx3.init()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        if collection.find_one({"username": username}):
            if collection.find_one({"password": password}):
                name = collection.find_one({"username": username}).get("name")
                useremail = collection.find_one({"username": username}).get("email")
                print("Login Successful")
                print(f"Hi {name}, Welcome Back {name}")
                text.say(f"Welcome Back {name}")
                text.runAndWait()
                sending_login(email=useremail)
                print('''1. Find Book
2. Send book Details to email
3. Reserved Book''')

                while True:

                    user_choice = int(input("Enter your choice: "))
                    if user_choice == 1:
                        um.find_book()

                    elif user_choice == 2:
                        um.sending_bookdetail(email = useremail, title = input("Enter your book title: "))

                    elif user_choice == 3:
                        um.reserved_book(email1 = useremail)


            else:
                print("Login Failed due to wrong password")
                return False
        else:
            print("Wrong Username")
            return False

    except Exception as e:
        print(f"An error occurred {e}")
        time.sleep(10)
        os.system("exit")
        return False


def username():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["User"]

    email1 = input("Enter your email: ")
    try:
        if collection.find_one({"email": email1}):
            if sending_otp(email=email1) == True:
                user_details = collection.find_one({"email": email1}).get('username')
                print(f"Your Username is {user_details}")
                print(f"Username send to your email")
                sending_username(email=email1, username=user_details)
            else:
                print("OTP Failed")
        else:
            print("No email found")

    except Exception as e:
        print(f"An error occurred {e}")


def password():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["User"]

    user_email = input("Enter your email: ")
    try:
        if collection.find_one({"email": user_email}):
            if sending_otp(email=user_email) == True:
                user_details = collection.find_one({"email": user_email}).get('password')
                print(f"Your Password is {user_details}")
                print(f"Password send to your email")
                sending_password(email=user_email, password1=user_details)
            else:
                print("OTP Failed")
        else:
            print("No email found")

    except Exception as e:
        print(f"An error occurred {e}")


def update():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Library_Management_System"]
    collection = db["User"]

    print("""1. Phone Number
2. Username
3. Password""")

    user_input = input("Enter your Email id: ")

    try:

        if collection.find_one({"email": user_input}):
            if sending_otp(email=user_input) == True:
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    update_user_number = input("Enter your phone number you want to update: ")
                    update_1 = {"$set": {"phone": update_user_number}}
                    update_2 = collection.find_one({"email": user_input})
                    update_3 = update_2.get("phone")
                    update_4 = {"phone": update_3}
                    collection.update_one(update_4, update_1)
                    print("Update Successful")

                if user_choice == "2":
                    update_username = input("Enter your username you want to update: ")
                    update_1 = {"$set": {"phone": update_username}}
                    update_2 = collection.find_one({"email": user_input})
                    update_3 = update_2.get("username")
                    update_4 = {"username": update_3}
                    collection.update_one(update_4, update_1)
                    print("Update Successful")

                if user_choice == "3":
                    update_password = input("Enter your password you want to update: ")
                    update_1 = {"$set": {"phone": update_password}}
                    update_2 = collection.find_one({"email": user_input})
                    update_3 = update_2.get("password")
                    update_4 = {"password": update_3}
                    collection.update_one(update_4, update_1)
                    print("Update Successful")


        else:
            print("No email found")


    except Exception as e:
        print(f"An error occurred {e}")


