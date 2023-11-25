from random import randint


def encode(word: str, shift: int) -> str:
    return ''.join([chr(ord(char) + shift) for char in word])


def main():
    user_data = input("Enter the file path: ")

    user_shift = input("Shift Param: ")
    try:
        shift = int(user_shift)
    except ValueError:
        print("\nInvalid input for shift parameter. Choosing a random shift.")
        shift = randint(1, 50)

    try:
        with open(user_data, encoding='utf8', mode='r') as file:
            content = file.read()
            encoded_data = encode(content, shift=shift)

            new_file_name = user_data.split('.')[0] + '_encoded.txt'
            with open(new_file_name, mode='w', encoding='utf8') as new_file:
                new_file.write(encoded_data)

            print(
                f"File encoded and saved as '{new_file_name}':\n{encoded_data}")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
