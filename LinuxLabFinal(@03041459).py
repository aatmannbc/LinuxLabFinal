import sys

class MessageEncoder:
    def __init__(self, shift):
        self.shift = shift
#Encoder Function
    def encode(self, message):
        encoded_message = ""
        for letter in message:
            if letter.isalpha():
                shifted_ascii = ord(letter.upper()) + self.shift
                if shifted_ascii > ord('Z'):
                    shifted_ascii -= 26
                encoded_message += chr(shifted_ascii)
        return encoded_message

class OutputFormatter:
    def __init__(self, block_size):
        self.block_size = block_size
#Formatting Function
    def format(self, message):
        formatted_message = ""
        block_count = 0
        for i, letter in enumerate(message):
            if i > 0 and i % self.block_size == 0:
                formatted_message += " "
                block_count += 1
                if block_count == 10:
                    formatted_message += "\n"
                    block_count = 0
            formatted_message += letter
        formatted_message += "\n"
        return formatted_message
#Main Function
def main(shift):
    encoder = MessageEncoder(int(shift))
    formatter = OutputFormatter(5)

    message = input("Enter message: ")
    message = message.upper()
    encoded_message = encoder.encode(message)
    formatted_message = formatter.format(encoded_message)

    print(formatted_message)

if __name__ == '__main__':
    main(sys.argv[1])