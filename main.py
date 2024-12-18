# Ethan Lawrence
# Password validation project
# Dec 16 2024

def check_length(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    else:
        return
def check_first_five(password):
    if  len(password) >= 5 and not password[0:5].isalpha():
        return
    else:
        return "Password must have number in first 5 characters."
def check_last_three(password):
    if  len(password) >= 3 and not password[-3:].isdigit():
        return
    else:
        return "Password must not have number in last 3 characters."
def check_no_special_characters(password):
    for character in password:
        if not (character.isalpha() or character.isdigit()):
            return 'Password cannot contain special characters or symbols!.'
    else:
        return
def check_for_letter(password):
    for character in password:
        if character.isalpha():
            return
    else:
        return 'Password must contain at least one letter!'
def check_for_number (password):
    for character in password:
        if character.isdigit():
            return
    else:
        return 'Password must contain at least one number!'

# Main
def main ():
    password = input('Please enter your password:\n')

    password_check = [
    check_length(password),
    check_first_five(password),
    check_last_three(password),
    check_for_letter(password),
    check_for_number(password),
    check_no_special_characters(password)
    ]
    
    errors = []

    for result in password_check:
        if result is not None:
            errors.append(result)
    
    if errors:
        for error in errors:
            print(error)
    else:
        print(f'Your password is: {password}')

if __name__ == '__main__':
    main()