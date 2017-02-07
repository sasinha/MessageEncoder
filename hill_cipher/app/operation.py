
from hill_cipher.app import cipher


def cipher_operation(operation_type, message):

    if operation_type == 'e':
        dimension = int(input("What dimension would you like your key to be? "))
        encrypted = cipher.encrypt(message, dimension)
        print("Encrypted message: ", encrypted[0])
        print("Key: ", encrypted[1])

    elif operation_type == 'd':
        key = input("What is your key? ")
        decrypted = cipher.decrypt(message, key)
        print("Unscrambled message: ", decrypted)

