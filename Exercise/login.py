users = [
    ['admin', 'admin002'],
    ['ram', 'ram002'],
    ['sita', 'sita002'],
    ['hari', 'hari002'],
]
username = input("Enter username: ")
password = input("Enter password: ")
total_users = len(users)
increment = 0
login_status = False
while increment < total_users:
    uname = users[increment][0]
    upass = users[increment][1]
    if uname == username and upass == password:
        login_status = True
        break
    increment += 1
if login_status == True:
    print(f"Welcome {username}")
else:
    print("Login Failed")
