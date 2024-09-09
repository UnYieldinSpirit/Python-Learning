import art
# program tasked with performing a caesar cipher on a message. ability to encrypt/decrypt

alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(original_msg, shift):
    final_msg = ""
    for char in original_msg:
        if char in alphabet: # uses this code to create the encoded letters, not numbers nor symbols.
            index_position = alphabet.index(char) # finds the letter in the text's alphabet position
            index_position += shift # creates the shift in the letter index position

            while index_position > len(alphabet) - 1: # while the index_position is out of the bounds of the alphabet list...
                index_position -= len(alphabet) # continuously subtracts the amount of the alphabet list until it is within the bounds of the 

            char = alphabet[index_position] # replaces the letter with the shifted letter
            final_msg += char
        else: # does nothing but instead just tacks the stuff into the final message wherever in the loop we are
            final_msg += char # adds the character to the encoded message
    return final_msg

def decode(original_msg, shift):
    final_msg = ""
    shift = -shift
    for char in original_msg:
        if char in alphabet:
            index_position = alphabet.index(char) # finds the letter in the text's alphabet position
            index_position += shift # creates the shift in the letter index position

            while index_position < -len(alphabet):
                index_position += len(alphabet)
            char = alphabet[index_position] # replaces the letter with the shifted letter
            final_msg += char # creates the decode msg
        else:
            final_msg += char
    return final_msg

def restart():
    answer = input("Would you like to continue? ('y'/'n') ")
    
    if answer == 'y':
        return True
    else:
        return False

def casear(original_msg, shift, direction):
    if direction == "encode":
        final_msg = encode(original_msg, shift)
        print(f"Here is the encoded result: {final_msg}")
    else:
        final_msg = decode(original_msg, shift)
        print(f"Here is the decoded result: {final_msg}")

try_again = True

print(art.logo)

while try_again == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    casear(text, shift, direction)
    try_again = restart()

print("Thanks for participating!")