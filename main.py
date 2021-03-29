from art import logo
from os import system

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(user_input, shift_ammount, option):
    output = ""
    for char in user_input:
        # addresses the problem of spaces/characters/numbers in user input(text), if the character is
        # in the alphabete it will encode them
        # other characters are part of the else statment and are just outputed to the output variable
        if char in alphabet:
            # this explained is: if char is "W", index will be 22, this + shift will cause index out of range
            # on the (alphabet), even if shift is a low number
            # -len(alphabet) always makes sure the index doesn't go above 26 this case, 22 + 25 - 26 = 22
            x = alphabet.index(char) + shift_ammount - len(alphabet)
            if option == "decode":
                x = alphabet.index(char) - shift_ammount
            output += alphabet[x]
        else:
            output += char
    print(f"The {option}d text is ({output})")


again = True


while again is True:

    system("clear")
    print(f"\033[31m{logo}\033[00m")
    # fixes a wrong input on (direction), only allow for "encode" or "decode"
    while True:
        direction = input("Type \033[93m'encode'\033[00m to encrypt, type \033[93m'decode'\033[00m to decrypt:\n")
        if direction == "encode" or direction == "decode":
            break
        else:
            print(f"\nPlease type 'ENCODE' or 'DECODE'\n")
            continue
    text = input("Type your message:\n").lower()
    # fixes the input as anything but an integer
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("\nPlease input a full number\n")
            continue
        else:
            break
            # solves the problem of hight shift number that would generate error
    if shift % 26 == 0:
        shift = len(text) % 10
    else:
        shift = shift % 26
    caesar(text, shift, direction)

    question = input("\nDo you want to run 'Caesar Cipher' again? (Y)es or (N)o :\n").lower()
    if question == "n":
        again = False
