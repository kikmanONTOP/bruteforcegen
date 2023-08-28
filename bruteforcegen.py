import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    file_name = input("Enter the name of the text file to be created: ")
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter a password length: "))

    with open(file_name, 'w') as file:
        for _ in range(num_passwords):
            password = generate_password(password_length)
            file.write(password + '\n')

    print(f"The file '{file_name}' was created with {num_passwords} passwords of length {password_length} characters.")

if __name__ == "__main__":
    main()