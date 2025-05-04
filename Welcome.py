import admin
import user


print('''1.Library Admin
2. User Login''')

user1 = int(input("Enter your choice:"))

if user1 == 1:
    print('''1.Register
2.Login
3.Retrived Username
4.Retrived Password
5.Update Details''')
    user2 = int(input("Enter your choice:"))
    if user2 == 1:
        admin.register()

    elif user2 == 2:
        admin.login()

    elif user2 == 3:
        admin.username()

    elif user2 == 4:
        admin.password()

    elif user2 == 5:
        admin.update()

    else:
        print("Wrong Choice")

elif user1 == 2:
    print('''1.Register
2.Login
3.Retrived Username
4.Retrived Password
5.Update Details''')
    user3 = int(input("Enter your choice:"))
    if user3 == 1:
        user.register()

    elif user3 == 2:
        user.login()

    elif user3 == 3:
        user.username()

    elif user3 == 4:
        user.password()

    elif user3 == 5:
        user.update()
    else:
        print("Wrong Choice")

else:
    print("Wrong Choice")
