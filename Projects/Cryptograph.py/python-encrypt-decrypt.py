## Using pyAesCrypt

# ipmort the module

from cryptography.fernet import Fernet

# Generate the key

key = Fernet.generate_key()

# put the key in a file " string "

with open('filekey.key', 'wb') as filekey:

    filekey.write(key)

# open the key

with open('filekey.key', 'rb') as filekey:

    key = filekey.read()

# using the generated key

fernet = Fernet(key)

# open original file

with open('example.csv', 'rb') as file:

    original = file.read()

# encrypt the file

encrypted = fernet.encrypt(original)

#open the file in write mode and write the encrypted data

with open('example.csv', 'wb') as file_encrypted:

    file_encrypted.write(encrypted)

# Using the key

fernet = Fernet(key)

# open the encrypted file

with open('example.csv', 'rb') as file_enc:

    encrypted = file_enc.read()

# decrypting the file

decrypted = fernet.decrypt(encrypted)

#open the file in write mode and write the encrypted data

with open('example.csv', 'wb') as file_dec:

    file_dec.write(decrypted)


## Using pyAesCrypt

import pyAesCrypt

# encryption / decryption buffer size - 64K

bufferSize = 64 *1024

password = "foopassword"

# encrypt

pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize)

# decrypt

pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)

