import random
import string

class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self):
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password

def user_interface():
    print("--- Password Generator ---")
    while True:
        try:
            length = int(input("Enter the desired password length (min 8): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        generator = PasswordGenerator(length)
        password = generator.generate_password()
        print(f"Generated Password: {password}")
        
        choice = input("Do you want to generate another password? (y/n): ")
        if choice.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    user_interface()
