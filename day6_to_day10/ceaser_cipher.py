"""Todo 1: Create a function called encrypt() that takes 
original_text and shift_amount as two  inputs"""
"""Todo 2: Inside the encrypt() function, shift each letter 
of the original_text forwards in the alphabet by the shift_amount
and print the encrypted text"""


def encrypt(original_text, shift_amount):
    alphabet = [
        "A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]
    original_text_upper = original_text.upper()
    encrypted_text = ""

    for i in original_text_upper:
        if i in alphabet:
            index = alphabet.index(i)+shift_amount
            if index > len(alphabet)-1:
                index = index % len(alphabet)
                encrypted_letter = alphabet[index]
                encrypted_text += encrypted_letter
   
            else:
                encrypted_letter = alphabet[index]
                encrypted_text += encrypted_letter

        else:
            encrypted_text += " "
        
    
    print(f'The encoded world is: {encrypted_text}')



"""Todo 3: Decode using same logic."""

def decrypt(original_text, shift_amount):
    alphabet = [
        "A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]
    original_text_upper = original_text.upper()
    encrypted_text = ""

    for i in original_text_upper:
        if i in alphabet:
            index = alphabet.index(i)-shift_amount
            if index > len(alphabet)-1:
                index = index % len(alphabet)
                encrypted_letter = alphabet[index]
                encrypted_text += encrypted_letter
   
            else:
                encrypted_letter = alphabet[index]
                encrypted_text += encrypted_letter

        else:
            encrypted_text += " "
        
    
    print(f'The decoded world is: {encrypted_text}')


print("""
CEASAR CIPHER
""")


while True:
    user_input = str(input("Type 'encode' or 'decode' to start order '0' to stop the program: "))

    if user_input == "encode":
        text = str(input("Type your message: "))
        shift = int(input("Type the shift number: "))
        encrypt(original_text=text, shift_amount=shift)

    elif user_input == "decode":
        text = str(input("Type your message: "))
        shift = int(input("Type the shift number: "))
        decrypt(original_text=text, shift_amount=shift)

    elif user_input == "0":
        print("Program stopped.")
        break   

    elif user_input != "encode" or "decode":
        print("Invalid input. Please try again.")