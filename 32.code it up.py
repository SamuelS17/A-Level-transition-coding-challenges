En_or_De = input("Would you like to encode or decode a string? (e/d): ")
if En_or_De == 'e':
    key = 25
    plaintext = input("Enter the text: ")
    encryption = ''
    for i in plaintext:
        if ord(i.lower())+key > 122:
            encryption += chr(ord(i)+key-26)
        else:
            encryption += chr(ord(i)+key)
    print(encryption)

elif En_or_De == 'd':
    encryption = input("Enter the encrypted text: ")
    key = 25
    plaintext = ''
    for i in encryption:
        if ord(i.lower())-key < 97:
            plaintext += chr(ord(i)-key+26)
        else:
            plaintext += chr(ord(i)-key)
    print(plaintext)