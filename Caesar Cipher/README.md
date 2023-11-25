#  🏛️ Caesar's Cipher Palace 🗝️

## Description
🎭 The Caesar Cipher is like a secret code game played by Julius Caesar back in ancient times! Imagine each letter in your message going on a fun adventure through the alphabet. They take steps to the right or left based on a secret number Caesar chose. So, if he picked "3," A becomes D, B becomes E, and so on!

## How it Works
The cipher operates by substituting each letter in the plaintext with a letter a fixed number of positions down or up the alphabet. For instance, with a shift of 3, A becomes D, B becomes E, and so on. It's a simple yet effective way of encoding messages.

## Usage
To use the Caesar Cipher:
1. Choose a shift value (the number of positions to shift each letter).
2. Input your message in plaintext.
3. Encrypt the message by shifting each letter by the chosen value to create the cipher text.
4. To decrypt, apply the reverse shift to the cipher text to reveal the original message.

## Example
- Shift: 3
- Plain Text: HELLO
- Encrypted Text: KHOOR

## File Structure and Contents

### `caesar_cipher.py`
This file contains functions for encoding and decoding messages using the Caesar Cipher. It provides methods:
- `encode(word: str, shift: int) -> str`: Encodes a string by shifting each character by a given value.
- `decode(word: str, shift: int) -> str`: Decodes an encoded string by shifting characters in the opposite direction.

### `encode.py`
This script allows encoding text from a file or direct input. It includes:
- A function `encode(word: str, shift: int) -> str` for encoding a given string by a specified shift value.
- User input to encode data either from a file or direct text input.
- If encoding from a file, it creates a new file with the encoded content appended by '_encoded.txt'.

### `decode.py`
This script facilitates decoding text from a file or direct input. It consists of:
- A function `decode(word: str, shift: int) -> str` for decoding an encoded string by a specified shift value.
- User input to decode data either from a file or direct text input.
- If decoding from a file, it creates a new file with the decoded content appended by '_decoded.txt'.


## `decode_shift.py`
This script attempts to decode encoded messages using a "Brute Force Attack" method. It provides:
- A function `decode(word: str, shift: int) -> str` to decode a string using a specified shift value.
- The script iterates through all possible shifts within the range of [1, 26] and displays the decoded messages for each shift.


### `example.txt`
This file contains an example text that can be used to test the encoding and decoding functionalities provided by the scripts.

## How to Use
1. **Encoding using `encode.py`:**
   - Run `python encode.py`.
   - Enter the file path or the text you want to encode.
   - Input the desired shift value or let the system choose a random one.
   - The encoded text will be displayed and saved in a new file if encoding from a file.

2. **Decoding using `decode.py`:**
   - Run `python decode.py`.
   - Enter the file path or the text you want to decode.
   - Input the same shift value used for encoding.
   - The decoded text will be displayed and saved in a new file if decoding from a file.

3. **Cracking Encoding using `decode_shift.py`**
   - Run `python decode_shift.py`.
   - Enter the encoded data you wish to decode.
   - The script will attempt all possible shifts and display the decoded messages for each shift.

## Further Information
For more details on the Caesar Cipher and its implementation, you can explore additional resources online or refer to cryptography books.

## Author
Created by **Utkarsh Saxena (DeepNets)**