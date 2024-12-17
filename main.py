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
        print("Password must have number in first 5 characters.")
def check_last_three(password):
    if  len(password) >= 3 and not password[-3:].isdigit():
        return
    else:
        print("Password must not have number in last 3 characters.")
def check_no_special_characters(password):
    for character in password:
        if not (character.isalpha() or character.isdigit()):
            print('Password cannot contain special characters or symbols!.')
            break
    else:
        return
def check_for_letter(password):
    for character in password:
        if character.isalpha():
            return
    else:
        print('Password must contain at least one letter!')
def check_for_number (password):
    for character in password:
        if character.isdigit():
            return
    else:
        print('Password must contain at least one number!')
password = 'Abcd2re4'
check_length(password)
check_first_five(password)
check_last_three(password)
check_for_letter(password)
check_for_number(password)
check_no_special_characters(password)
print('Reading complete')