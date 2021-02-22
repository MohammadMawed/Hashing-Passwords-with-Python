
import hashlib

print("Enter your password:")

password = input()

hashedpassword = hashlib.sha256(str.encode(password)).hexdigest()

print(hashedpassword)