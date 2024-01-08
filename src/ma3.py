# Function to encode a message by shifting each character's ASCII value by 1
def encode(message):
    encoded_message = ""
    for char in message:
        encoded_char = chr(ord(char) + 1)  # Shift the character's ASCII value by 1
        encoded_message += encoded_char    # Append the encoded character to the encoded message
    return encoded_message

def decode(encoded_message):
    message = ''
    for char in encoded_message:
        message += chr(ord(char) - 1)
    return message

# Main function of the program
def main():
    action = input()
    message = input()                 

    if action == 'c':
        encoded_message = encode(message)
        print("Encoded message:", encoded_message)
    elif action == 'd':
        decoded_message = decode(message)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid action.")  # Display an error message for invalid actions

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the encoding/decoding process