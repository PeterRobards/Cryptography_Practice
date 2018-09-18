#!/usr/bin/env python3
"""This script encrypts and decrypts user provided plaintext"""
# -*- coding: utf-8 -*-
#
# Cipher Program -- Version 4.0
# Copyright (c) 2020 Peter Robards
#
##########################################################################################
#
# usage: Cipher.py [-h] [-E] [-D] [-f] [-i INPUTFILE] [-o OUTPUTFILE]
#                    [-S {left,right}] [-T {Caesar,Substitution,Vigenere}]
#
# optional arguments:
#  -h, --help            show this help message and exit
#  -E, --encrypt         Signals that user wants to encrypt text.
#  -D, --decrypt         Signals that user wants to decrypt text.
#  -f, --file            File used as source with results saved to new File.
#  -i INPUTFILE, --input_from_file INPUTFILE
#                        Load text from the provided file name.
#  -o OUTPUTFILE, --output_to_file OUTPUTFILE
#                        Save results to the provided file name.
#  -S {left,right}, --shift {left,right}
#                        Choose between 'right' or 'left' direction for key
#                        shift. Default = "right"
#  -T {Caesar,Substitution,Vigenere}, --type {Caesar,Substitution,Vigenere}
#                       Choose between encryption methods. Default = "Caesar"
#
##########################################################################################
#
# Based on the following Extended 95 Character Set:
#   abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#   character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits
#    + " " + string.punctuation
#
##########################################################################################

import sys
import string
import random
import argparse


# Method to Encrypt and/or Decrypt Text via a Caesar Cipher
def caesar_cipher(
    text, key, characters=string.ascii_lowercase, decrypt=False, shift_type="right"
):
    """Encrypt and/or Decrypt Text via a Caesar Cipher"""
    if key < 0:

        print("ERROR - Key value: ", key, " cannot be negative!")

        return None

    size = len(characters)

    if decrypt:

        key = size - key

    if shift_type == "left":

        # if left shift is desired, we simply inverse they sign of the key
        key = -key

    # Python string method maketrans() returns a translation table that maps each character
    #  in the intab (string with original characters) into the character at the same position
    #  in the outtab (string with corresponding mapping character).
    #  Returns a translate table to be used translate() function - called below.
    table = str.maketrans(characters, characters[key:] + characters[:key])

    # Python string method translate() returns a copy of the string in which all characters
    #  have been translated using table (constructed with the maketrans() method used above)
    translated_text = text.translate(table)

    return translated_text


# Method to Encrypt and/or Decrypt Text via a complex substitution with a keyword
# via a Vigenere Cipher
def vigenere_cipher(
    text, key, characters=string.ascii_lowercase, decrypt=False, shift_type="right"
):
    """Encrypt and/or Decrypt Text with a keyword via a Vigenere Cipher"""

    translated_text = ""

    # Determine length of key
    size = len(key)
    # Initialize array for our key values the same size as the key
    key_values = [0] * size

    # Iterate through each of the letters in the key string
    i = 0  # used to assign track position in key_values array
    for letter in key:
        # find() returns first occurrence of letter in our characters lookup table
        #  assigns index value to key_values
        key_values[i] = characters.find(letter)

        i += 1

    # iterate over each character in the plain text
    j = 0  # used to record the count of characters within plain text processed so far
    for letter in text:

        k_shift = key_values[j % size]  # decide which key value is to be used

        if decrypt:
            ## if decrypt is desired, we simply inverse they sign of the key
            k_shift = -k_shift

        if shift_type == "left":
            # if left shift is desired, we begin from the left side of our character lest
            k_shift = size - k_shift

        # Python string method maketrans() returns a translation table that maps each character
        #  in the intab (string with original characters) into the character at the same position
        #  in the outtab (string with corresponding mapping character).
        #  Returns a translate table to be used translate() function - called below.
        table = str.maketrans(characters, characters[k_shift:] + characters[:k_shift])

        # Python string method translate() returns a copy of the string in which all characters
        #  have been translated using table (constructed with the maketrans() method used above)
        translated_text += letter.translate(table)

        j += 1

    return translated_text


# Method that creates a slice that starts at the end of provided string,
#  and moves backwards to reverse it.
#  []::-1] means start at the end of the string and end at position 0,
#  move with the step -1, negative one, which means one step backwards
def reverse_string(text):
    """ Reverse the provided string of characters"""
    return text[::-1]


# Method that converts a string to list and shuffle it to mix letters and digits
#  Depends on random library
def shuffle(sample_str):
    """ converts a string to list and shuffle it to mix letters and digits"""
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = "".join(sample_list)

    return final_string


# Method to Encrypt and/or Decrypt Text via a simple or complex substitution Cipher
def substitution_cipher(
    text, cipher_alphabet, characters=string.ascii_lowercase, decrypt=False
):
    """Encrypt and/or Decrypt Text via a simple or complex substitution Cipher"""
    # Check that cipher alphabet and character set has the same number of elements
    if len(characters) != len(cipher_alphabet):
        print(
            "\nERROR -> Cipher Alphbet must contain the same number of elements as character set!"
        )
        print(
            "\n\t Cipher Alphabet : ",
            len(cipher_alphabet),
            "\n\t Character Set : ",
            len(characters),
        )
        print(
            "\nCharacter Set : \t",
            characters,
            "\nCipher Alphabet : \t",
            cipher_alphabet,
        )
        sys.exit("\nPlease check both settings and retry - thank you!\n")
    # if default cipher alphabet is used and it matches the character set exactly,
    #  reverse it for some security
    if characters == cipher_alphabet:
        cipher_alphabet = reverse_string(cipher_alphabet)

    if decrypt:
        # Python string method maketrans() returns a translation table that maps each character
        #  in the intab (string with original characters) into the character at the same position
        #  in the outtab (string with corresponding mapping character).
        #  Returns a translate table to be used translate() function - called below.
        table = str.maketrans(cipher_alphabet, characters)
    else:
        # Python string method maketrans() returns a translation table that maps each character
        #  in the intab (string with original characters) into the character at the same position
        #  in the outtab (string with corresponding mapping character).
        #  Returns a translate table to be used translate() function - called below.
        table = str.maketrans(characters, cipher_alphabet)

    # Python string method translate() returns a copy of the string in which all characters
    #  have been translated using table (constructed with the maketrans() method used above)
    translated_text = text.translate(table)

    return translated_text


# Method to get KEY number from user
def get_cipher_alphabet(characters=string.ascii_lowercase):
    """get KEY number from user"""
    cipher_alphabet = ""

    print("\nPlease select one of the following options for your Cipher Alphabet:")
    print("\n\t1. Generate Simple Reversed Character set [1].")
    print("\n\t2. Generate an original Random  Character set [2].")
    print("\n\t3. Enter Your Own Custom Character set [3].")

    while True:
        num = input("\nPlease make your choice [1, 2, or 3]: ")
        try:
            choice = int(num)
            print("\nThank You!\n")

            if choice == 1:
                cipher_alphabet = reverse_string(characters)
                break
            elif choice == 2:
                cipher_alphabet = shuffle(characters)
                print(
                    "\nHere is the Random Cipher Alphabet\
                    - Please Record it or Decryption may not be possible!"
                )
                print("\nCipher Alphabet:\n\t", cipher_alphabet)
                break
            elif choice == 3:
                print(
                    "\n\n Please enter Cipher Alphabet of length: (",
                    len(characters),
                    ")",
                )
                cipher_alphabet = input("\n\t:")
                break
            else:
                print("\nERROR - Choice: ", num, ", is invalid!\n")
                print("Please enter a valid Choice: [1, 2, or 3]!")

        except ValueError:
            print("\nERROR - Choice: ", num, ", is invalid!\n")
            print("Please enter a valid Choice: [1, 2, or 3]!")

    while True:
        answer = input(
            "\nWould you like to save the Cipher Alphabet to file? [Yes or No]: "
        )

        if answer[0].lower() == "y":
            output_file = input("\nPlease enter path for output file\n\t:")
            output_to_file(output_file, cipher_alphabet)
            break
        elif answer[0].lower() == "n":
            break
        else:
            print("\nERROR - your response", answer, " is invalid!\n")
            print('\nPlease type either "Yes" or "No"!\n')

    return cipher_alphabet


# Method to Encrypt and/or Decrypt a File filled with text via a simple substitution (Caesar) Cipher
def file_cipher(
    file_name,
    output_file_name,
    key,
    characters=string.ascii_lowercase,
    decrypt=False,
    shift_type="right",
    enc_type="Caesar",
):
    """Encrypt and/or Decrypt a File filled with text via a simple substitution (Caesar) Cipher"""
    with open(file_name, "r") as f_in:

        with open(output_file_name, "w") as f_out:

            # iterate over each line in input file
            for line in f_in:

                # encrypt/decrypt the line
                if enc_type == "Caesar":
                    line_new = caesar_cipher(line, key, characters, decrypt, shift_type)
                elif enc_type == "Vigenere":
                    line_new = vigenere_cipher(
                        line, key, characters, decrypt, shift_type
                    )
                elif enc_type == "Substitution":
                    line_new = substitution_cipher(line, key, characters, decrypt)

                # write the new line to output file
                f_out.write(line_new)

    print(
        "The file {} has been translated successfully and saved to {}".format(
            file_name, output_file_name
        )
    )


# Method to read input from a specified file
def input_from_file(file_name):
    """reads input from a specified file"""
    with open(file_name, "r") as file:
        text = file.read().replace("\n", "")

    print("\nYour text has been retreived from: {}".format(file_name))

    return text


# Method to save output to a specified file
def output_to_file(file_name, text):
    """write output to a specified file"""
    with open(file_name, "w") as file:
        # write the new line to output file
        file.write(text)

    print("\nThe results have been saved to: {}".format(file_name))


# Method to get KEY number from user and check to make sure it is valid
def get_key(key_type):
    """get KEY number from user and check to make sure it is valid"""
    if key_type == "Caesar":
        while True:
            num = input("\nPlease enter an integer for Cipher to utilize as a key : ")
            try:
                key = int(num)
                print("\nThank You!")
                break
            except ValueError:
                print("\nERROR - Input", num, " is invalid!\n")
                print("Please enter a valid integer!")

    elif key_type == "Vigenere":
        key = input(
            "\nPlease enter word or phrase for the Cipher to utilize as a key : "
        )

    return key



###############################################################

######################## Main Function ########################
def main():
    """Main Method: checks for user supplied args and generates password from supplied parameters"""

    #### Define optional command line arguments to tweak password settings via argparse library ####
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-E",
        "--encrypt",
        dest="encrypt",
        action="store_true",
        help="Signals that user wants to encrypt text.",
    )
    parser.add_argument(
        "-D",
        "--decrypt",
        dest="decrypt",
        action="store_true",
        help="Signals that user wants to decrypt text.",
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        action="store_true",
        help="File used as source with results saved to new File.",
    )
    parser.add_argument(
        "-i",
        "--inputfile",
        dest="inputfile",
        help="Load text from the provided file name.",
    )
    parser.add_argument(
        "-o",
        "--outputfile",
        dest="outputfile",
        help="Save results to the provided file name.",
    )
    parser.add_argument(
        "-S",
        "--shift",
        dest="shift",
        choices=["left", "right"],
        default="right",
        help="Choose between 'right' or 'left' direction for key shift. Default = \"right\" ",
    )
    parser.add_argument(
        "-T",
        "--type",
        dest="type",
        choices=["Caesar", "Substitution", "Vigenere"],
        default="Caesar",
        help='Choose between encryption methods. Default = "Caesar" ',
    )

    ####

    # Initialize command line arguments
    args = parser.parse_args()

    # assign SHIFT direction choice using either default value or user preferred option
    SHIFT = args.shift
    # assign encryption method choice using either default value or user preferred option
    TYPE = args.type

    # Create simple Lookup Table consisting of all lowercase and uppercase alphanumeric characters
    #  plus common punctuation and spaces:
    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    character_set = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + " "
        + string.punctuation
    )

    # print("\nExtended character set:\n", character_set)

    if args.encrypt:
        DECRYPT = False

        if args.file:

            if args.inputfile:
                infile = args.inputfile
            else:
                infile = input("\nPlease enter path to input file\n\t:")

            if args.outputfile:
                outfile = args.outputfile
            else:
                outfile = input("\nPlease enter path for output file\n\t:")

            if TYPE == "Substitution":
                KEY = get_cipher_alphabet(character_set)
            else:
                KEY = get_key(TYPE)

            print("\n\t**** ENCRYPTING ****\n")
            file_cipher(
                infile,
                outfile,
                KEY,
                character_set,
                decrypt=DECRYPT,
                shift_type=SHIFT,
                enc_type=TYPE,
            )

        else:

            if args.inputfile:
                infile = args.inputfile
                plain_text = input_from_file(infile)
            else:
                plain_text = input("\nPlease enter text to encrypt\n\t:")
                # plain_text = "We ATTACK at Dawn. Rendezvous at 95th street and bring supplies!"

            if TYPE == "Substitution":
                KEY = get_cipher_alphabet(character_set)
            else:
                KEY = get_key(TYPE)

            print("\n\t**** ENCRYPTING ****\n")
            print("\nPlain text:\n", plain_text)

            if TYPE == "Caesar":
                encrypted = caesar_cipher(
                    plain_text, KEY, character_set, decrypt=DECRYPT, shift_type=SHIFT
                )
            elif TYPE == "Vigenere":
                encrypted = vigenere_cipher(
                    plain_text, KEY, character_set, decrypt=DECRYPT, shift_type=SHIFT
                )
            elif TYPE == "Substitution":
                encrypted = substitution_cipher(
                    plain_text, KEY, character_set, decrypt=DECRYPT
                )

            print("\n\t**** SUCCESS! ****\n")
            print("\nEncrypted text:\n", encrypted)

            if args.outputfile:
                outfile = args.outputfile
                output_to_file(outfile, encrypted)


    elif args.decrypt:
        DECRYPT = args.decrypt

        if args.file:

            if args.inputfile:
                infile = args.inputfile
            else:
                infile = input("\nPlease enter path to input file\n\t:")

            if args.outputfile:
                outfile = args.outputfile
            else:
                outfile = input("\nPlease enter path for output file\n\t:")

            if TYPE == "Substitution":
                KEY = get_cipher_alphabet(character_set)
            else:
                KEY = get_key(TYPE)

            print("\n\t**** DECRYPTING ****\n")
            file_cipher(
                infile,
                outfile,
                KEY,
                character_set,
                decrypt=DECRYPT,
                shift_type=SHIFT,
                enc_type=TYPE,
            )

        else:

            if args.inputfile:
                infile = args.inputfile
                cipher_text = input_from_file(infile)
            else:
                cipher_text = input("\nPlease enter text to decrypt\n\t:")

            if TYPE == "Substitution":
                KEY = get_cipher_alphabet(character_set)
            else:
                KEY = get_key(TYPE)

            print("\n\t**** DECRYPTING ****\n")
            print("\ncipher text:\n", cipher_text)

            if TYPE == "Caesar":
                decrypted = caesar_cipher(
                    cipher_text, KEY, character_set, decrypt=DECRYPT, shift_type=SHIFT
                )
            elif TYPE == "Vigenere":
                decrypted = vigenere_cipher(
                    cipher_text, KEY, character_set, decrypt=DECRYPT, shift_type=SHIFT
                )
            elif TYPE == "Substitution":
                decrypted = substitution_cipher(
                    cipher_text, KEY, character_set, decrypt=DECRYPT
                )

            print("\n\t**** SUCCESS! ****\n")
            print("\nDecrypted text:\n", decrypted)

            if args.outputfile:
                outfile = args.outputfile
                output_to_file(outfile, decrypted)

    else:
        DECRYPT = False

        print("\n\t**** Default setting is to Encrypt! ****\n")

        if args.file:

            if args.inputfile:
                infile = args.inputfile
            else:
                infile = input("\nPlease enter path to input file\n\t:")

            if args.outputfile:
                outfile = args.outputfile
            else:
                outfile = input("\nPlease enter path for output file\n\t:")

            if TYPE == "Substitution":
                KEY = get_cipher_alphabet(character_set)
            else:
                KEY = get_key(TYPE)

            print("\n\t**** ENCRYPTING ****\n")
            file_cipher(
                infile,
                outfile,
                KEY,
                character_set,
                decrypt=DECRYPT,
                shift_type=SHIFT,
                enc_type=TYPE,
            )

        else:

            if args.inputfile:
                infile = args.inputfile
                plain_text = input_from_file(infile)
            else:
                plain_text = input("\nPlease enter text to encrypt\n\t:")
                # plain_text = "We ATTACK at Dawn. Rendezvous at 95th street and bring supplies!"

            if TYPE == "Substitution":
                KEY = get_cipher_alphabet(character_set)
            else:
                KEY = get_key(TYPE)

            print("\n\t**** ENCRYPTING ****\n")
            print("\nPlain text:\n", plain_text)

            if TYPE == "Caesar":
                encrypted = caesar_cipher(
                    plain_text, KEY, character_set, decrypt=DECRYPT, shift_type=SHIFT
                )
            elif TYPE == "Vigenere":
                encrypted = vigenere_cipher(
                    plain_text, KEY, character_set, decrypt=DECRYPT, shift_type=SHIFT
                )
            elif TYPE == "Substitution":
                encrypted = substitution_cipher(
                    plain_text, KEY, character_set, decrypt=DECRYPT
                )

            print("\n\t**** SUCCESS! ****\n")
            print("\nEncrypted text:\n", encrypted)

            if args.outputfile:
                outfile = args.outputfile
                output_to_file(outfile, encrypted)


    print("\n")


######################## Driver Code ########################
if __name__ == "__main__":

    # Call main function
    main()
