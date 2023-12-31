import os

# Generate 32 random bytes and convert them to a hexadecimal string
random_hex = os.urandom(32).hex()
print(random_hex)
