from random import randint

# Function to encode a string


def encode(word: str, shift: int) -> str:
    return ''.join([chr(ord(char) + shift) for char in word])

# Function to decode a string


def decode(word: str, shift: int) -> str:
    return ''.join([chr(ord(char) - shift) for char in word])


def main():
    user_input = input("Enter the word or file path to encode: ")

    try:
        shift = int(input("Enter the shift parameter: "))
    except ValueError:
        print("Invalid shift parameter. Please enter an integer.")
        return

    try:
        with open(user_input, encoding='utf8', mode='r') as file:
            content = file.read()
            encoded_data = encode(content, shift=shift)

            # Write encoded data back to file
            with open(user_input, mode='w', encoding='utf8') as f:
                f.write(encoded_data)

            print("File encoded successfully!")

            decode_choice = input("\nDo you want to decode it? (yes/no): ")
            if decode_choice.lower() == "yes":
                decoded_data = decode(encoded_data, shift=shift)
                print(f"Decoded Word: {decoded_data}")

    except FileNotFoundError:
        encoded_word = encode(user_input, shift=shift)
        print(f"Encoded Word: {encoded_word}")

        decode_choice = input("\nDo you want to decode it? (yes/no): ")
        if decode_choice.lower() == "yes":
            decoded_word = decode(encoded_word, shift=shift)
            print(f"Decoded Word: {decoded_word}")


if __name__ == "__main__":
    main()
