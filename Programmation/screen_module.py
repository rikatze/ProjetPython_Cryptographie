"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""

import screen_constants


def show_start_ask_language():
    """
    asks the language the user wants to use at the beginning:french or english
    ' f ' for french
    ' e ' for english
    :return: char
    """
    return input(screen_constants.START_ASK_LANGUAGE)


def show_language_settings():
    """
    asks the language the user wants to use in the program : french or english
    ' f ' for french
    ' e ' for english
    :return: char
    """
    return input(screen_constants.LANGUAGE_SETTINGS)


def show_main_menu(english):
    """
    asks the user if he wants to use the fonction encryption or decryption of the program
    'c' for encryption
    'd' for decryption
    's' for going to language settings
    'q' to quit the program
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        return input(screen_constants.ENGLISH_MAIN_MENU)
    # language chosen is french
    elif not english:
        return input(screen_constants.FRENCH_MAIN_MENU)
    else:
        return "this should never happen"


def show_principles(english, encrypting):
    """
    asks what type of method the user wants to use to encrypt or decrypt his text
    'c' for Caesar's cypher
    'v' for Vigenere's cypher
    'e' for the Enigma machine
    'm' to go back to the main menu
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :param encrypting: boolean
    True if the user wants to encrypt his text
    False if he wants to decrypt his text
    :return: char
    """
    # language chosen is english
    if english:
        if encrypting:
            return input(screen_constants.ENGLISH_PRINCIPLES_ENCRYPTING)
        if encrypting is False:
            return input(screen_constants.ENGLISH_PRINCIPLES_DECRYPTING)
    # language chosen is french
    elif not english:
        if encrypting:
            return input(screen_constants.FRENCH_PRINCIPLES_ENCRYPTING)
        if encrypting is False:
            return input(screen_constants.FRENCH_PRINCIPLES_DECRYPTING)
    else:
        return "this should never happen"


def show_ask_key(english, principle):
    """
    asks the key the user wants to use for the method his has chosen
    key = char
    ' m ' to go back to the main menu
    :param principle:
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        if principle == 'c':
            return input(screen_constants.ENGLISH_ASK_KEY_CAESAR)
        elif principle == 'v':
            return input(screen_constants.ENGLISH_ASK_KEY_VIGENERE)
        elif principle == 'e':
            return input(screen_constants.ENGLISH_ASK_KEY_ENIGMA)
        else:
            return "this should never happen"
    # language chosen is french
    elif not english:
        if principle == 'c':
            return input(screen_constants.FRENCH_ASK_KEY_CAESAR)
        elif principle == 'v':
            return input(screen_constants.FRENCH_ASK_KEY_VIGENERE)
        elif principle == 'e':
            return input(screen_constants.FRENCH_ASK_KEY_ENIGMA)
        else:
            return "this should never happen"


def show_ask_text(english):
    """
    asks the text that the user wants to decrypt/encrypt
    ' m ' to go back to the main menu
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        return input(screen_constants.ENGLISH_ASK_TEXT)
    # language chosen is french
    elif not english:
        return input(screen_constants.FRENCH_ASK_TEXT)
    else:
        return "this should never happen"


def show_treated_text(english, encrypting, text):
    """
    shows the decrypted/encrypted text
    :param text: string
    the user's en-/decrypted text
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :param encrypting: boolean
    True if the user wants to encrypt his text
    False if he wants to decrypt his text
    :return: char
    """



def show_continue(english):
    """
    shows the help screen which give explanations on the different encryption methods
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        input(screen_constants.ENGLISH_CONTINUE)
    # language chosen is french
    elif not english:
        input(screen_constants.FRENCH_CONTINUE)
    else:
        return "this should never happen"


def show_quit_message(english):
    """
    shows the exit message of the program
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        print(screen_constants.ENGLISH_QUIT_MESSAGE)
    # language chosen is french
    elif not english:
        print(screen_constants.FRENCH_QUIT_MESSAGE)
    else:
        return "this should never happen"
