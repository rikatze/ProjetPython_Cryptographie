"""
This module contains all functions with which the user's text can be treated.
"""


# TODO: COMMENT CODE!!!


# ************************************* begin CAESAR ***********************************************************s****** #
# *** ENCRYPTION *** #
def encrypt_caesar(text, key):
    """
    encrypts and returns the given text by using the principle of Caesar
    :param text: user's text (string)
    :param key: user's key (number)
    :return: text: encrypted text
    """
    encrypted_text = ''
    for i in text:
        if ord(i) + key > 90:
            i = chr(ord('A') - 1 + (key - (ord('Z') - ord(i))))
            encrypted_text += i
        else:
            i = chr(ord(i) + key)
            encrypted_text += i
    return encrypted_text


# *** DECRYPTION *** #
def decrypt_caesar(text, key):
    # TODO add description
    """
    decrypts and returns the given text by using the principle of Caesar
    :param text: user's text (string)
    :param key: user's key (number)
    :return: text: decrypted text
    """
    decrypted_text = ''
    for i in text:
        if ord(i) - key < 65:
            i = chr(ord('Z') + 1 - (key - (ord(i) - ord('A'))))
            decrypted_text += i
        else:
            i = chr(ord(i) - key)
            decrypted_text += i
    return decrypted_text


# ************************************ end CAESAR ******************************************************** #


# ********************************** begin VIGENERE ****************************************************** #
# *** HELP FUNCTIONS *** #
def create_vigenere_table():
    # TODO: add description
    """

    :return:
    """
    # TODO voluntarily: change to range
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    table = []
    for k in range(26):
        table += [alphabet[k:] + alphabet[:k]]
    return table


def create_table_text_key(text, key):
    """
    creates a table with the user's text in the first line and the repeated key in the second
    :param text: string
    :param key: string
    :return: table
    """
    key = key.upper()
    repeated_key = ""
    while len(repeated_key) < len(text):
        repeated_key += key
    list_key = []
    for i in range(len(text)):
        list_temp = [text[i], repeated_key[i]]
        list_key.append(list_temp)
    return list_key


# *** ENCRYPTION *** #
def encrypt_vigenere(text, key):
    # TODO add description
    """
    encrypts and returns the given text by using the principle of Vigenere
    :param text: user's text (string)
    :param key: user's key (string)
    :return: text: encrypted text
    """
    table_of_vigenere = create_vigenere_table()
    repeated_key_table = create_table_text_key(text, key)
    encrypted_text = ""
    # TODO voluntarily: change to range
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(text)):
        text_letter = repeated_key_table[i][0]
        key_letter = repeated_key_table[i][1]
        encrypted_text += table_of_vigenere[alphabet.index(text_letter)][alphabet.index(key_letter)]
    return encrypted_text


# *** DECRYPTION *** #
def decrypt_vigenere(text, key):
    # TODO add description
    """

    :param text:
    :param key:
    :return:
    """
    table_of_vigenere = create_vigenere_table()
    repeated_key_table = create_table_text_key(text, key)
    decrypted_text = ""
    # TODO voluntarily: change to range
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(text)):
        letter_text = repeated_key_table[i][0]
        letter_key = repeated_key_table[i][1]
        list_temp = table_of_vigenere[alphabet.index(letter_key)]
        decrypted_text += alphabet[list_temp.index(letter_text)]
    return decrypted_text


# ****** end VIGENERE ****** #


# ********** begin ENIGMA ********** #
# *** HELP FUNCTIONS *** #
# * General functions * #
def create_initial_list():
    """
    creates a list filled with the alphabet (capital letters)
    :return: list
    """
    # real list:
    # initial_list = [chr(x) for x in range(65, 91)]
    # for test purpose used letters are only "A - F"
    initial_list = [chr(x) for x in range(65, 71)]
    return initial_list


def search_index(initial_list, letter, offset):
    """
    searches the index of a given letter in the given list
    :param offset: the rotor's offset of the enigma machine
    :param initial_list: list for searching
    :param letter: index of this letter is wanted
    :return: index of the letter
    """
    i = 0
    # index initialized with 999 because
    # if something goes wrong in the loop the program stops after the execution of this function
    index = 999

    while i < len(initial_list):
        if initial_list[i] == letter:
            index = i
            break
        i += 1
    else:
        index += offset
        if (index < 0) or (index > len(initial_list)):
            index %= len(initial_list)

        # check if sth went wrong before
        if index > len(initial_list):
            return "This should never happen"
        else:
            return index


def plugboard(letter):
    """
    represents the plugboard, i. e. checks if a given letter is plugged to another.
    If yes returns this letter, if no returns the given letter.
    :param letter: the given letter (char)
    :return: letter: either the plugged or the given letter (char)
    """
    # In this case the plugboard's setting is the one of the 31th of a month,
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    # the plug combination is:
    # A-H, B-L, C-X, D-I, E-R, F-K, G-U, N-P, O-Q, T-Y
    # (J, M, S, V, W and Z not plugged)
    if letter in "JMSVWZ":
        return letter
    elif letter in "A":
        return "H"
    elif letter in "B":
        return "L"
    elif letter in "C":
        return "X"
    elif letter in "D":
        return "I"
    elif letter in "E":
        return "R"
    elif letter in "F":
        return "K"
    elif letter in "G":
        return "U"
    elif letter in "N":
        return "P"
    elif letter in "O":
        return "Q"
    elif letter in "T":
        return "Y"
    else:
        return "This should never happen"


def permutation_reflector(letter):
    """
    represents the reflector, i. e. returns the corresponding letter of the given letter
    :param letter: char
    :return: letter: char
    """
    # In this case the reflector's setting is the one of roller 'A',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Machine)'
    # the permutation is the following:
    # A-E, B-J, C-M, D-Z, F-L, G-Y, H-X, I-V, K-W, N-R, O-Q, P-U, S-T (and in the other direction)
    if letter in "A":
        return "E"
    elif letter in "B":
        return "J"
    elif letter in "C":
        return "M"
    elif letter in "D":
        return "Z"
    elif letter in "E":
        return "A"
    elif letter in "F":
        return "L"
    elif letter in "G":
        return "Y"
    elif letter in "H":
        return "X"
    elif letter in "I":
        return "V"
    elif letter in "J":
        return "B"
    elif letter in "K":
        return "W"
    elif letter in "L":
        return "F"
    elif letter in "M":
        return "C"
    elif letter in "N":
        return "R"
    elif letter in "O":
        return "Q"
    elif letter in "P":
        return "U"
    elif letter in "Q":
        return "O"
    elif letter in "R":
        return "N"
    elif letter in "S":
        return "T"
    elif letter in "T":
        return "S"
    elif letter in "U":
        return "P"
    elif letter in "V":
        return "I"
    elif letter in "W":
        return "K"
    elif letter in "X":
        return "H"
    elif letter in "Y":
        return "G"
    elif letter in "Z":
        return "D"
    else:
        return "This should never happen"


# * functions representing the rotors * #
# encryption
def shift_first_rotor_encryption(initial_list, index):
    """
    represents the letter shift of the first rotor and returns the corresponding letter
    :param initial_list: list on which the function operates
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'I',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    if index == 0:
        return initial_list[index + 4]
    elif index in (1, 7, 13):
        return initial_list[index + 9]
    elif index in (2, 14):
        return initial_list[index + 10]
    elif index in (3, 12):
        return initial_list[index + 2]
    elif index in (4, 16):
        return initial_list[index + 7]
    elif index == 5:
        return initial_list[index + 1]
    elif index == 6:
        return initial_list[index - 3]
    elif index == 8:
        return initial_list[index + 13]
    elif index == 9:
        return initial_list[index + 16]
    elif index in (10, 17):
        return initial_list[index + 3]
    elif index == 11:
        return initial_list[index + 8]
    elif index == 15:
        return initial_list[index - 8]
    elif index == 18:
        return initial_list[index]
    elif index == 19:
        return initial_list[index - 4]
    elif index == 20:
        return initial_list[index - 20]
    elif index == 21:
        return initial_list[index - 13]
    elif index == 22:
        return initial_list[index - 21]
    elif index == 23:
        return initial_list[index - 6]
    elif index == 24:
        return initial_list[index - 22]
    elif index == 25:
        return initial_list[index - 16]
    else:
        return "This should never happen"


def shift_second_rotor_encryption(initial_list, index):
    """
    represents the letter shift of the second rotor and returns the corresponding letter
    :param initial_list: list on which the function operates
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'II',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    if index in (0, 16):
        return initial_list[index]
    elif index == 1:
        return initial_list[index + 8]
    elif index in (2, 10):
        return initial_list[index + 1]
    elif index in (3, 18):
        return initial_list[index + 7]
    elif index == 4:
        return initial_list[index + 14]
    elif index in (5, 21):
        return initial_list[index + 3]
    elif index == 6:
        return initial_list[index + 11]
    elif index == 7:
        return initial_list[index + 13]
    elif index == 8:
        return initial_list[index - 8]
    elif index == 9:
        return initial_list[index + 1]
    elif index == 11:
        return initial_list[index - 4]
    elif index == 12:
        return initial_list[index + 10]
    elif index == 13:
        return initial_list[index + 6]
    elif index in (14, 23):
        return initial_list[index - 2]
    elif index == 15:
        return initial_list[index - 13]
    elif index == 17:
        return initial_list[index - 11]
    elif index == 19:
        return initial_list[index - 6]
    elif index == 20:
        return initial_list[index - 5]
    elif index == 22:
        return initial_list[index - 17]
    elif index == 24:
        return initial_list[index - 10]
    elif index == 25:
        return initial_list[index - 21]
    else:
        return "This should never happen"


def shift_third_rotor_encryption(initial_list, index):
    """
    represents the letter shift of the third rotor and returns the corresponding letter
    :param initial_list: list on which the function operates
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'III',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    if index == 0:
        return initial_list[index + 1]
    elif index == 1:
        return initial_list[index + 2]
    elif index == 2:
        return initial_list[index + 3]
    elif index == 3:
        return initial_list[index + 4]
    elif index in (4, 17):
        return initial_list[index + 5]
    elif index == 5:
        return initial_list[index + 6]
    elif index == 6:
        return initial_list[index - 4]
    elif index == 7:
        return initial_list[index + 8]
    elif index == 8:
        return initial_list[index + 9]
    elif index in (9, 11, 14):
        return initial_list[index + 10]
    elif index in (10, 12):
        return initial_list[index + 13]
    elif index == 13:
        return initial_list[index]
    elif index in (15, 25):
        return initial_list[index - 11]
    elif index in (16, 24):
        return initial_list[index - 8]
    elif index == 18:
        return initial_list[index - 12]
    elif index == 19:
        return initial_list[index - 19]
    elif index == 20:
        return initial_list[index - 10]
    elif index == 21:
        return initial_list[index - 9]
    elif index == 22:
        return initial_list[index - 2]
    elif index == 23:
        return initial_list[index - 5]
    else:
        return "This should never happen"


# decryption
def shift_first_rotor_decryption(initial_list, index):
    """
    represents the letter shift of the first rotor and returns the corresponding letter
    :param initial_list: list on which the function operates
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'I',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    if index == 0:
        return initial_list[index - 4]
    elif index in (1, 7, 13):
        return initial_list[index - 9]
    elif index in (2, 14):
        return initial_list[index - 10]
    elif index in (3, 12):
        return initial_list[index - 2]
    elif index in (4, 16):
        return initial_list[index - 7]
    elif index == 5:
        return initial_list[index - 1]
    elif index == 6:
        return initial_list[index + 3]
    elif index == 8:
        return initial_list[index - 13]
    elif index == 9:
        return initial_list[index - 16]
    elif index in (10, 17):
        return initial_list[index - 3]
    elif index == 11:
        return initial_list[index - 8]
    elif index == 15:
        return initial_list[index + 8]
    elif index == 18:
        return initial_list[index]
    elif index == 19:
        return initial_list[index + 4]
    elif index == 20:
        return initial_list[index + 20]
    elif index == 21:
        return initial_list[index + 13]
    elif index == 22:
        return initial_list[index + 21]
    elif index == 23:
        return initial_list[index + 6]
    elif index == 24:
        return initial_list[index + 22]
    elif index == 25:
        return initial_list[index + 16]
    else:
        return "This should never happen"


def shift_second_rotor_decryption(initial_list, index):
    """
    represents the letter shift of the second rotor and returns the corresponding letter
    :param initial_list: list on which the function operates
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'II',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    if index in (0, 16):
        return initial_list[index]
    elif index == 1:
        return initial_list[index - 8]
    elif index in (2, 10):
        return initial_list[index - 1]
    elif index in (3, 18):
        return initial_list[index - 7]
    elif index == 4:
        return initial_list[index - 14]
    elif index in (5, 21):
        return initial_list[index - 3]
    elif index == 6:
        return initial_list[index - 11]
    elif index == 7:
        return initial_list[index - 13]
    elif index == 8:
        return initial_list[index + 8]
    elif index == 9:
        return initial_list[index - 1]
    elif index == 11:
        return initial_list[index + 4]
    elif index == 12:
        return initial_list[index - 10]
    elif index == 13:
        return initial_list[index - 6]
    elif index in (14, 23):
        return initial_list[index + 2]
    elif index == 15:
        return initial_list[index + 13]
    elif index == 17:
        return initial_list[index + 11]
    elif index == 19:
        return initial_list[index + 6]
    elif index == 20:
        return initial_list[index + 5]
    elif index == 22:
        return initial_list[index + 17]
    elif index == 24:
        return initial_list[index + 10]
    elif index == 25:
        return initial_list[index + 21]
    else:
        return "This should never happen"


def shift_third_rotor_decryption(initial_list, index):
    """
    represents the letter shift of the third rotor and returns the corresponding letter
    :param initial_list: list on which the function operates
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'III',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    if index == 0:
        return initial_list[index - 1]
    elif index == 1:
        return initial_list[index - 2]
    elif index == 2:
        return initial_list[index - 3]
    elif index == 3:
        return initial_list[index - 4]
    elif index in (4, 17):
        return initial_list[index - 5]
    elif index == 5:
        return initial_list[index - 6]
    elif index == 6:
        return initial_list[index + 4]
    elif index == 7:
        return initial_list[index - 8]
    elif index == 8:
        return initial_list[index - 9]
    elif index in (9, 11, 14):
        return initial_list[index - 10]
    elif index in (10, 12):
        return initial_list[index - 13]
    elif index == 13:
        return initial_list[index]
    elif index in (15, 25):
        return initial_list[index + 11]
    elif index in (16, 24):
        return initial_list[index + 8]
    elif index == 18:
        return initial_list[index + 12]
    elif index == 19:
        return initial_list[index + 19]
    elif index == 20:
        return initial_list[index + 10]
    elif index == 21:
        return initial_list[index + 9]
    elif index == 22:
        return initial_list[index + 2]
    elif index == 23:
        return initial_list[index + 5]
    else:
        return "This should never happen"


# *** ENCRYPTION *** #
def encrypt_enigma(text, key):
    """
    encrypts and returns the given text by using the principle of the Enigma machine
    :param text: user's text (string)
    :param key: user's key (string composed of three letter)
    :return text: encrypted text
    """
    # #################### TODO: think about # KEY ??? ###############
    initial_list = create_initial_list()

    offset_first_rotor = 0
    offset_second_rotor = 0
    offset_third_rotor = 0
    encrypted_text = ""
    index_of_letter = 0

    for letter in text:
        # ** forward path **
        # plugboard
        letter = plugboard(letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_first_rotor)
        # first rotor
        letter = shift_first_rotor_encryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_second_rotor)
        # second rotor
        letter = shift_second_rotor_encryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_third_rotor)
        # third rotor
        letter = shift_third_rotor_encryption(initial_list, index_of_letter)

        # permutation reflector
        letter = permutation_reflector(letter)

        # ** return path **
        # determine index
        index_of_letter = search_index(initial_list, letter, offset_third_rotor)
        # third rotor
        letter = shift_third_rotor_encryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_second_rotor)
        # second rotor
        letter = shift_second_rotor_encryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_first_rotor)
        # first rotor
        letter = shift_first_rotor_encryption(initial_list, index_of_letter)

        # plugboard
        letter = plugboard(letter)

        # add encrypted letter to the encrypted text
        encrypted_text = encrypted_text + letter

        # change offset variables
        offset_first_rotor -= 1
        if offset_first_rotor == ((-1) * len(initial_list)):
            offset_first_rotor = 0
            offset_second_rotor -= 1
            if offset_second_rotor == ((-1) * len(initial_list)):
                offset_second_rotor = 0
                offset_third_rotor -= 1
                if offset_third_rotor == ((-1) * len(initial_list)):
                    offset_third_rotor = 0
                else:
                    pass
            else:
                pass
        else:
            pass

    return encrypted_text


# *** DECRYPTION *** #
def decrypt_enigma(text, key):
    """
    decrypts and returns the given text by using the principle of the Enigma machine
    :param text: user's text (string)
    :param key: user's key (string composed of three letter)
    :return text: decrypted text
    """
    # #################### TODO: think about # KEY ??? ###############
    initial_list = create_initial_list()

    offset_first_rotor = 0
    offset_second_rotor = 0
    offset_third_rotor = 0
    decrypted_text = ""
    index_of_letter = 0

    for letter in text:
        # ** forward path **
        # plugboard
        letter = plugboard(letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_first_rotor)
        # first rotor
        letter = shift_first_rotor_decryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_second_rotor)
        # second rotor
        letter = shift_second_rotor_decryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_third_rotor)
        # third rotor
        letter = shift_third_rotor_decryption(initial_list, index_of_letter)

        # permutation reflector
        letter = permutation_reflector(letter)

        # ** return path **
        # determine index
        index_of_letter = search_index(initial_list, letter, offset_third_rotor)
        # third rotor
        letter = shift_third_rotor_decryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_second_rotor)
        # second rotor
        letter = shift_second_rotor_decryption(initial_list, index_of_letter)

        # determine index
        index_of_letter = search_index(initial_list, letter, offset_first_rotor)
        # first rotor
        letter = shift_first_rotor_decryption(initial_list, index_of_letter)

        # plugboard
        letter = plugboard(letter)

        # add encrypted letter to the encrypted text
        decrypted_text = decrypted_text + letter

        # change offset variables
        offset_first_rotor -= 1
        if offset_first_rotor == ((-1) * len(initial_list)):
            offset_first_rotor = 0
            offset_second_rotor -= 1
            if offset_second_rotor == ((-1) * len(initial_list)):
                offset_second_rotor = 0
                offset_third_rotor -= 1
                if offset_third_rotor == ((-1) * len(initial_list)):
                    offset_third_rotor = 0
                else:
                    pass
            else:
                pass
        else:
            pass

    return decrypted_text


# ********** end ENIGMA ********** #


encrypt_enigma("ADECADECADEC", "")
# decrypt_enigma("", "")
