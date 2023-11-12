#Нахождение номера телефона
import re

def extract_phone_numbers(text):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

def main():
    text = """
    Привет! Мой номер телефона 123-456-7890, если он не доступен, то
    вы можете связаться со мной по номеру 987-654-3210. Хорошего дня!
    """
    phone_numbers = extract_phone_numbers(text)
    print("Найденные номера телефонов:")
    for number in phone_numbers:
        print(number)

if __name__ == "__main__":
    main()