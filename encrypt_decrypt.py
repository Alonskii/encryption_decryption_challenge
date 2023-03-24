import random, time
#A basic encryption algorithm...
def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for i in range(0,len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + character
        for j in range (0,key):
            ciphertext = ciphertext + random.choice(alphabet)
            return ciphertext

#Main program starts here...
#Input...
plaintext = input("Enter a message to encrypt (plaintext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (key>=1 and key<=10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))

#Process... 
print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)

ciphertext = encrypt(plaintext, key)
#Output...
print("Ciphertext:")
print(ciphertext)


time.sleep(5)

ciphertext = input('please enter a text to decrypt: ')
key = int(input('Please enter a key: '))

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(0, len(ciphertext)):
        if i % (key + 1) == 0:
            plaintext += ciphertext[i]
    return plaintext


while (key < 1 or  key > 10): 
    print("Please enter correct key...")
    key = int(input('Please enter a key: '))


plaintext = decrypt(ciphertext, key)

print("...")
time.sleep(1)
print("Decrypting Cipher Text...")
print("...")
time.sleep(1)

print(f"Decrypted Text: {plaintext}")
