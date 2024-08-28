# program tasked with performing a caesar cipher on a message. ability to encrypt/decrypt

alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode(original_msg, shift):
    final_msg = ""
    for char in original_msg:
        index_position = alphabet.index(char) # finds the letter in the text's alphabet position
        index_position += shift # creates the shift in the letter index position

        while index_position > len(alphabet) - 1: # while the index_position is out of the bounds of the alphabet list...
            index_position -= len(alphabet) # continuously subtracts the amount of the alphabet list until it is within the bounds of the 

        char = alphabet[index_position] # replaces the letter with the shifted letter
        final_msg += char # creates the encoded msg
    return final_msg

def decode(original_msg, shift):
    final_msg = ""
    for char in original_msg:
        index_position = alphabet.index(char) # finds the letter in the text's alphabet position
        index_position -= shift # creates the shift in the letter index position
        char = alphabet[index_position] # replaces the letter with the shifted letter
        final_msg += char # creates the decode msg
    return final_msg

def casear(original_msg, shift, direction):  
    if direction == "encode":
        final_msg = encode(original_msg, shift)
        print(f"Here is the encoded result: {final_msg}")
    else:
        final_msg = decode(original_msg, shift)
        print(f"Here is the decoded result: {final_msg}")

casear(text, shift, direction)