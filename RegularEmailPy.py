#Провека email
import re

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def main():
    email = input("Введите email: ")
    if check_email(email):
        print("Email валиден.")
    else:
        print("Email невалиден.")

if __name__ == "__main__":
    main()