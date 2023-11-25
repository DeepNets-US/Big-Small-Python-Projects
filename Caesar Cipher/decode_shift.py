def decode(word: str, shift: int) -> str:
    return ''.join([chr((ord(char) - shift)) for char in word])


def decode_from_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            print("\nDecoded Messages:")
            for i in range(1, 26):
                decoded_data = decode(data, shift=i)
                print(f'Key : {i:2} \tDecoded: {decoded_data}')
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("""
                    !! Note !!
    This program can only function if the key chosen in the initial encoding process lies between [0, 25].
    This process checks all possible combinations within the [1, 26] range. Once all decoded strings are available, the user can find the original message. This method is called "Brute Force Attack".
    """)

    user_input = input(
        "Enter '1' to decode from file or '2' to enter data manually: ")

    if user_input == '1':
        file_path = input("Enter the file path to decode: ")
        decode_from_file(file_path)
    elif user_input == '2':
        data = input("Enter the data to decode: ")
        print("\nDecoded Messages:")
        for i in range(1, 26):
            print(f'Key : {i:2} \tDecoded: {decode(data, shift=i)}')
    else:
        print("Invalid input. Please enter '1' or '2'.")


if __name__ == '__main__':
    main()
