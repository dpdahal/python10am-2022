users = [
    {'id': 1, 'name': 'admin', 'gender': 'male', 'status': 1},
    {'id': 2, 'name': 'laxmi', 'gender': 'female', 'status': 0},
    {'id': 3, 'name': 'madana', 'gender': 'male', 'status': 1},
    {'id': 4, 'name': 'diyan', 'gender': 'male', 'status': 1},
    {'id': 5, 'name': 'sita', 'gender': 'female', 'status': 1},
    {'id': 6, 'name': 'anil', 'gender': 'male', 'status': 1},

]
total_users = len(users)
total_male = 0
total_female = 0
total_active_user = 0
total_active_male = 0
total_active_female = 0
total_inactive_male = 0
total_inactive_female = 0
for user in users:
    if user['gender'] == 'male':
        if user['status'] == 1:
            total_active_male += 1
        else:
            total_inactive_male += 1
        total_male += 1

    if user['gender'] == 'female':
        if user['status'] == 1:
            total_active_female += 1
        else:
            total_inactive_female += 1
        total_female += 1

    if user['status'] == 1:
        total_active_user += 1

print(f"Total user: {total_users}")
print(f"Total Male: {total_male}")
print(f"Total Female: {total_female}")
print(f"Total Active: {total_active_user}")
print(f"Total Active Male:  {total_active_male}")
print(f"Total Active Female:  {total_active_female}")
print(f"Total Inactive Male:  {total_inactive_male}")
print(f"Total Inactive Female:  {total_inactive_female}")
