def decode(word: str, shift: int) -> str:
    return ''.join([chr(ord(char) - shift) for char in word])


def main():
    user_data = input("Enter the file path to decode: ")

    try:
        shift = int(input("Shift Param: "))
    except ValueError:
        print("Invalid shift parameter. Please enter an integer.")
        return

    try:
        with open(user_data, encoding='utf8', mode='r') as f:
            content = f.read()
            decoded_data = decode(content, shift=shift)

            new_file_name = user_data.split('.')[0] + '_decoded.txt'
            with open(new_file_name, mode='w', encoding='utf8') as new_file:
                new_file.write(decoded_data)

            print(
                f"File Decoded and saved as '{new_file_name}':\n{decoded_data}")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
