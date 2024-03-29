MAX_KEY_SIZE=26

def getMode():
    while True:
        print "Do you wish to encrypt or decrypt a message?"
        mode=raw_input().lower()
        if mode=='encrypt' or mode=='e' or mode=='decrypt' or mode=='d':
            return mode
    else:
        print "Either enter 'encrypt' or 'e' or 'decrypt' or 'd'"

def getMessage():
    print "Enter your message:"
    return raw_input()

def getKey():
    key=0
    while True:
        print "Enter the key number (1-%s)" %(MAX_KEY_SIZE)
        key=input()
        if (key>=1 and key <=MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode=='d' or mode=='decrypt':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
    
            translated += chr(num)
        else:
            translated += symbol
    return translated
    
mode = getMode()
message = getMessage()
key = getKey() 
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
 
