# ---100 Days of Code---
# -- Day 8 Project --

from cipher_art import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('logo\n')
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
word = str(input("Type your message:\n")).lower()
shift = int(input("Type the shift number:\n"))

def encrypt(input_text, shift_num):
    """
    Encrypts a word

    Inputs:
        encrypted_word (str): the user inputted word
        shift_num (int): the number of shits the user selected
    
    Returns: an encrypted word
    """
    #take the alphabet and shift it 
    encryped_word = ""
    for letter in input_text:
        if letter not in alphabet:
            encryped_word += letter 
        else:
            current_position = alphabet.index(letter)
            new_position = current_position + shift_num
            encrypted_letter = alphabet[new_position]
            encryped_word += encrypted_letter
    print(f"The encrypted message is {encryped_word}")

def decrypt(encryped_word, shift_num):
    """
    Decrypts an encrypted word

    Inputs:
        encrypted_word (str): the user inputted word
        shift (int): the number of shits the user selected

    Returns: a decrypted word
    """
    decrypted_word = ""
    for letter in encryped_word:
        if letter not in alphabet:
            decrypted_word += letter 
        else:
            current_position = encryped_word.index(letter)
            new_position = alphabet[current_position - shift_num]
            decryped_letter = alphabet[new_position]
            decrypted_word += decryped_letter
    print(f"The decrypted message is {decryped_letter}")

if direction == "encode":
    encrypt(word, shift)
else:
    decrypt(word, shift)


