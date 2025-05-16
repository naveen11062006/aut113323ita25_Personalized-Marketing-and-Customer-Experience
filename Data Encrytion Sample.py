from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

user_data = b"User symptoms: Headache and fever"
encrypted = cipher.encrypt(user_data)
decrypted = cipher.decrypt(encrypted)
