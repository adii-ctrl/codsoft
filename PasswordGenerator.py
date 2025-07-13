import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be at least 4 characters long."

    # Combine different character types
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("🔐 Welcome to the Python Password Generator!")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        password = generate_password(length)
        print(f"✅ Your generated password is: {password}")
        
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
