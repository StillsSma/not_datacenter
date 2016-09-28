import csv

with open('data.csv', 'rt') as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)




def login():
    successful_login = False

    while successful_login == False:
        username = input("username: ")
        password = input("password: ")

        for row in data:
            if username == row[0] and password == row[1]:
                    print("Login Accepted")
                    successful_login = True
                    break
            else:
                continue
        print("Login Not Accepted")

    answer = input("create user[c] or log out[l]?: ")

    if answer == "c":
        new_username = input("type new username: ")
        new_password = input("type new password: ")
        new_fullname = input("type full name: ")
        new_row = "{},{},{}".format(new_username,new_password,new_fullname)

        fd = open('data.csv', 'a')
        fd.write(new_row)
        fd.close()

    elif answer == "l":
        login()

login()
