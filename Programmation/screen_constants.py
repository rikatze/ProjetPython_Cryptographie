"""
This module contains all screen constants, i. e. all texts of the user interface.
"""

# constants for both languages
START_ASK_LANGUAGE = """         Hello. Welcome to the cryptography program

Please select your language:
             
'f' for Français, 'e' for English : """

LANGUAGE_SETTINGS = """         Please select your language:

'f' for Français,   'e' for English :  """

# English user interface
ENGLISH_MAIN_MENU = """         What do you want to do - encrypt or decrypt a message?

Enter 'c' for encrypting or 'd' for decrypting.

Enter 's' to change settings(language)

or 'q' to exit :(   :   """

ENGLISH_PRINCIPLES_ENCRYPTING = """         How do you want to encrypt your text?

Enter 'c' for Caesar's cypher,

enter 'v' for Vigenere's cypher

or enter 'e' for the encryption by the Enigma machine.

Enter 'h' if you want more informations about each method of encryption

Enter 'm' to go back to the main menu   :   """

ENGLISH_PRINCIPLES_DECRYPTING = """         How do you want to decrypt your text?

Enter 'c' for Caesar's cypher,

enter 'v' for Vigenere's cypher

or enter 'e' for the decryption by the Enigma machine.

Enter 'h' if you want more informations about each method of decryption

Enter 'm' to go back to the main menu    :   """

ENGLISH_ASK_KEY_CAESAR = """        You chose <<Caesar>>:

Please enter your key (a number between 1 and 25 included).

Enter 'm' to go back to the main menu

or 'r' to go back to the previous menu  :   """

ENGLISH_ASK_KEY_VIGENERE = """You chose <<Vigenere>>:

Please enter your key (a world).

Enter 'm' to go back to the main menu

or 'r' to go back to the previous menu :   """

ENGLISH_ASK_KEY_ENIGMA = """        You chose <<Enigma>>:

Please enter your key (composed of three upper case letters).

Enter 'm' to go back to the main menu

or 'r' to go back to the previous menu  :   """

ENGLISH_ASK_TEXT = """      Please enter your text.

Enter 'm' to go back to the main menu

or 'r' to go back to the previous menu. :   """
ENGLISH_ENCRYPTED_TEXT = """Here is your encrypted text:
"""
ENGLISH_DECRYPTED_TEXT = """Here is your decrypted text:
"""
ENGLISH_HELP_PRINCIPLES = """********************** HELP ***********************

These are explanations of the different encryption and decryption principles.

- Caesar's cypher:
This principle was invented by Julius Caesar for his private correspondence.
It is a type of substitution cipher in which each letter in the plaintext
is replaced by a letter some fixed number of positions down the alphabet.

- Vigenere's cypher:
This principle was invented in the 16th century by Blaise de Vigenere et is based on the use of Vigenere's table
(table which is filled twice by the alphabet). A key (a word) is repeated and put under the message and this way
you can find the corresponding letters in the table.

- The Enigma machine:
The Enigma machine is a cryptography machine invented by  Arthur Scherbius in 1919. It was used during the Second
World War for the private communication between the different forces of the German army. Enigma consists of five
rotors which include a reflector, a keyboard, a plugboard and lamps for each letter of the alphabet.
The cryptography principle is simple: When you enter a letter on the keyboard, a current flow is sent to the plugboard
in which the entered letter is turned in another letter if they are connected. The current flow will then pass
the first four rotors: There is a letter shift in each of the three middle rotors which is executed. After this the
letters are changed again in the reflector which sends them back through the rotors to the plugboard which permits
the corresponding lamp to the letter to light up."""

ENGLISH_QUIT_MESSAGE = """      Thank you for using our program.

Good bye and have a nice day."""

# French user interface
FRENCH_MAIN_MENU = """          Bonjour. Bienvenue sur le programme de cryptographie.

Que voulez-vous faire -crypter ou décrypter un message?

Insérez c pour crypter ou d pour décrypter.

Insérez s pour changer les paramètres(langue)

ou q pour quitter le programme :(   :   """

FRENCH_PRINCIPLES_ENCRYPTING = """         De quelle manière voulez-vous crypter votre texte?

Intérez 'c' pour le cryptage par la methode du chiffre de César,

insérez 'v' pour le cryptage par la méthode du chiffre de Vigenère

ou insérez 'e' pour le cryptage par la méthode de la machine Enigma.

Insérez 'h' si vous voulez plus d'informations sur les différentes méthodes de cryptage

Insérez 'm' pour retourner au menu principal    :   """

FRENCH_PRINCIPLES_DECRYPTING = """          De quelle manière voulez-vous décrypter votre texte?

Intérez 'c' pour le décryptage par la methode du chiffre de César,

insérez 'v' pour le décryptage par la méthode du chiffre de Vigenère

ou insérez 'e' pour le décryptage par la méthode de la machine Enigma.

Insérez 'h' si vous voulez plus d'informations sur les différentes méthodes de décryptage

Insérez 'm' pour retourner au menu principal    :   """

FRENCH_ASK_KEY_CAESAR = """         Vous avez choisi <<César>>:

Insérez votre clé (un nombre compris entre 1 et 25);

Insérez 'm' pour retourner au menu principal

ou 'r' pour retourner au dernier menu   :   """

FRENCH_ASK_KEY_VIGENERE = """           Vous avez choisi<<Vigenère:

Insérez votre clé (un mot).

Insérez 'm' pour retourner au menu principal

ou 'r' pour retourner au dernier menu   :   """

FRENCH_ASK_KEY_ENIGMA = """     Vous avez choisi <<Enigma>>:

Insérez votre clé (composée de trois lettres en majuscules).

Insérez 'm' pour retourner au menu principal

ou 'r' pour retourner au dernier menu   :   """

FRENCH_ASK_TEXT = """       Insérez votre texte.

Insérez 'm' pour retourner au menu principal    

ou 'r' pour retourner au dernier menu   :   """

FRENCH_ENCRYPTED_TEXT = """Voici votre texte crypté:
"""

FRENCH_DECRYPTED_TEXT = """Voici votre texte décrypté:
"""

FRENCH_HELP_PRINCIPLES = """******************** AIDE ***********************

Voici les explications pour les différents principes de (dé)cryptage.

- Le chiffre de César :
Ce procédé a été inventé lors de l'époque romaine par Jules César pour ses communications secrètes.
En décalant l'alphabet par un entier donné chaque lettre est associée à une nouvelle lettre, ainsi
on peut crypter le message initiale en remplaçant chaque lettre par la nouvelle lettre attribuée.

- Le chiffre de Vigenère :
Il a été inventé au 16e siècle par Blaise de Vigenère et est basé sur le tableau de Vigenère
(tableau avec deux fois l'alphabet). Une clé (un mot) est répétée et mise sous le message et
de cette manière on peut trouver les lettres correspondantes à partir du tableau.

- Le principe de la machine Enigma :
L’Enigma est une machine de cryptographie inventée par Arthur Scherbius en 1919. Elle a été utilisée
durant la Seconde Guerre mondiale pour la communication secrète entre les différentes unités de l’armée allemande.
La machine est constituée de cinq rotors dont un réflecteur, d’un clavier, d’un tableau de permutation et de
lampes pour chaque lettre. Pour l’allumer il faut une batterie de 4,5 Volt.
Le principe est simple : Lorsqu’on appuie sur une lettre du clavier, un courant électrique va être envoyé au
tableau de permutation dans lequel la lettre entrée est échangée avec une autre lettre si elles sont connectées.
Puis il passera la première fois par les quatre rotors : Dans chacun des trois rotors au milieu il y a un décalage
des lettres qui s’opère. À la fin les lettres sont permutées encore une fois dans le réflecteur qui les renvoie par
les rotors au tableau de permutation ce qui permettra à une lampe correspondant à une lettre de s’allumer.
Ainsi pour chaque lettre on relève la lettre codée, on obtient alors notre message crypté.

Insérez 'm' pour retourner au menu principal."""

FRENCH_QUIT_MESSAGE = """       Merci d'avoir utilisé notre programme.
Bonne journée, au revoir."""
