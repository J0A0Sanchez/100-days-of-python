"""Todo 1: combine the encrypt and decrypt functions into one
named ceaser()"""

"""Todo 2: fix to code for what if the user enter number/symbols
maintain it in the text"""

"""Todo 3: Make the user decide when stop by typing 'break' to stop"""


def ceaser(original_text, shift_amount, encode_or_decode):
    alphabet = [
        "A","B","C","D","E","F","G","H","I","J","K","L","M",
        "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ]
    original_text_upper = original_text.upper()
    encrypted_text = ""

    if encode_or_decode == "decode":
            shift_amount *=  -1

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
            encrypted_text += i
        
    
    print(f'The {encode_or_decode}d world is: {encrypted_text}')


#ceaser("JOAO^Vitor!test*** aaaaa",2,"encode")

user_input = str(input("Type 'encode' or 'decode' to start or 'break' to stop the program: "))

while True:
    if user_input == "break":
         break
    else:
        text = str(input("Type your message: "))
        shift = int(input("Type the shift number: "))
        ceaser(original_text=text, shift_amount=shift, encode_or_decode=user_input)
        user_input = str(input("Type 'encode' or 'decode' to start or 'break' to stop the program: "))

