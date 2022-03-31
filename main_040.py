#Password Checker

name = input('How would you like to be called? ')
password = input('Fill in your password? ')

password_length = len(password) 
hidden_password = '*' * password_length

print(f"Hey {name}, your password {hidden_password} has {password_length} characters.")