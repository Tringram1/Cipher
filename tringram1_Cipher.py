# Tierra Ingram
# 2/26/2023
# Comp163, Section 4
# "Cipher" Program to both encode and decode a user's input


while True: # While loop to continuoulsy run program

    encodeDic = {'a': 'm', 'b': 'p', 'c': 'r', 'd': 'v', 'e': 'k', 'f': 'y', 'g': 'h', 'h': 'n',
             'i': 'c', 'j': 'f', 'k': 'l', 'l': 'g', 'm': 'u', 'n': 'd', 'o': 'q', 'p': 'e', 
             'q': 't', 'r': 'j', 's': 'o', 't': 's', 'u': 'z', 'v': 'a', 'w': 'b', 'x': 'i',
             'y':'x', 'z':'w', '': ''} # Dictionary for both the encode and decode

    print() # Welcome menu
    print()
    print('Welcome to the Cipher Program!')
    choice = input('Would you like to Encode a message (Type 1)\nDecode a message (Type 2)\nOr stop the program? (Type 3) : ')


    if choice == '3': # Sentinel Value to break continuous loop
            print('You have ended the program')
            break
    
    if choice == '1' :
        print()
        user_input = input('Enter text characters for message (a-z) : ')
        textMsg = user_input.lower() 
        encodeMsg = ''

        for i in textMsg: # Iterates through user input, assigning characters to corresponing values in dictionary

            if i in encodeDic:
                encodeMsg += encodeDic.get(i) # Get method returns values in dictionary
            else:
                encodeMsg += ' ' # For spaces in the user input

        print(f'Your encoded message is : {encodeMsg}')


    decodeDic = dict([(value, key) for key, value in encodeDic.items()]) # Reverses orginal dictionary to swap keys with values

    if choice == '2' :
        print() 
        user_input = input('Enter text characters for message (a-z) : ')
        textMsg = user_input.lower()
        decodeMsg = ''

        for i in textMsg:
  
            if i in encodeDic:
                decodeMsg += decodeDic.get(i)

            else:
                decodeMsg += ' '
            
        print(f'Your decoded message is : {decodeMsg}')


        

    
















