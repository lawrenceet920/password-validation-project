# Ethan Lawrence
# Password validation project
# Dec 16 2024

def check_length(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    else:
        return
def check_first_five(password):
    if  len(password) >= 5 and not password[0:6].isalpha():
        return
    else:
        print("Password must have number in first 5 characters")
def check_last_three(password):
    if  len(password) >= 3 and not password[-3:].isdigit():
        return
    else:
        print("Password must not have number in last 3 characters")

password = '1eeeeepp1p123'
check_length(password)
check_first_five(password)
check_last_three(password)