import sys

def encode(message, shift):
    """Encodes a message using a Caesar Cipher with the given shift."""
    encoded_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr(((ord(char.upper()) - 65 + shift) % 26) + 65)
            encoded_message += shifted_char
    return encoded_message

if __name__ == "__main__":
    # Get the shift amount from the command line arguments
    shift = int(sys.argv[1])

    # Read the message from standard input
    message = input().strip()

    # Convert the message to uppercase and encode it
    encoded_message = encode(message.upper(), shift)

    # Print the encoded message in blocks of 5
    block_size = 5
    for i in range(0, len(encoded_message), block_size):
        print(encoded_message[i:i+block_size], end=" ")
        if (i+1) % (block_size*10) == 0:
            print()

    # Add a newline after the last line, if necessary
    if len(encoded_message) % (block_size*10) != 0:
        print()
