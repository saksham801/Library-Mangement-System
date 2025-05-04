
# Library Mangement System



## 1.Welcome.py

Acts as the main menu or entry point for the application. It allows the user to choose between Library Admin and User Login, and based on the choice, it directs to respective operations like Register, Login, Retrieve Username/Password, or Update Details.

## 2. admin.py
Handles functionality for library administrators, including:

• Registering new admins

• Logging in

• Retrieving forgotten usernames or passwords

• Updating admin details

## 3. user.py
Manages operations for regular users, similar to admin.py, including:

• User registration

• Login

• Retrieving usernames/passwords

• Updating personal details

## 4.main.py

Works as a connector or driver script that possibly handles high-level integration or testing between modules like book management, user management, or admin functionalities.

## 5. book.py
Manages all book-related operations in the library system, such as:

• Adding new books

• Displaying available books

• Issuing or returning books

• Searching for books

## 6.umangement.py
Responsible for user-side book interactions, such as:

• Viewing issued books

• Reserving books

• Interacting with the library system from a user's perspective

## 7.lmangement.py
Handles admin-side book and library management, including:

• Managing book inventory

• Viewing issued/reserved books by users

• Admin-related tracking and book allocation


## Install All Required Libries

To run install, run the following commond

```bash
  pip install pymongo
```
```bash
  pip install pyttsx3
```
```bash
  pip install string
```
```bash
  pip install smtplib
```
```bash
  pip install os
```
```bash
  pip install requests
```



## Contributing

Contributions are always welcome!

Welcome Just share the ideas or any problems on dubeysaksham801@gmail.com

Please adhere to this project's `code of conduct`.


## Features

- Sending OTPs And Verfiying
- Sending All Details of book to the User
- Sending Logins Details like Country , ip ,etc to the User or Admin
- All Are Free


## Feedback

If you have any feedback, please reach out to us at dubeysaksham801@gmail.com

