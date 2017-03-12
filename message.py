#Author: Andrew Bossie
#Encrypted Messages

originalChar = ord(input("Enter the unencrypted message."))

key = int(input("Enter key value, 0 - 100"))

if ((originalChar) + key) > 126:

    encryptedChar = (((originalChar) + Key) - 127) + 32

else:

    encryptedChar = (originalChar + Key)

print("Your encrypted message is", encryptedChar".")


#decryption
encryptedChar = ord(input("Enter encrypted message."))

key = int(input("Enter key value, 0 - 100"))

if (encryptedChar - Key < 32) then

    decryptedChar = ((encryptedChar - Key) + 127) - 32

else

    decryptedChar = (encryptedChar - Key)

print("Your decrypted message is", decryptedChar".")
