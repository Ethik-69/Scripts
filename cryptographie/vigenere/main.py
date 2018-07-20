#! /usr/bin/python
# -*- coding:utf-8 -*-
import os


def decryption(pos_letter, key, text):
    buffer = []
    new_text = ''
    i = 0
    for letter in text:
        if letter == ' ':
            buffer.append(' ')
        elif letter.lower() in pos_letter:
            if i == len(key):
                i = 0
            buffer.append(pos_letter[letter.lower()]-pos_letter[key[i]])
            i += 1

    for i in range(len(buffer)):
        if buffer[i] == ' ':
            new_text += ' '
        elif buffer[i] < 1:
            buffer[i] += 26

        new_text += ''.join([key for key, valeur in pos_letter.items() if valeur == buffer[i]])

    return new_text


def encryption(pos_letter, key, text):
    buffer = []
    new_text = ''
    i = 0
    for letter in text:
        if letter == ' ':
            buffer.append(' ')
        elif letter.lower() in pos_letter:
            if i == len(key):
                i = 0
            buffer.append(pos_letter[letter.lower()]+pos_letter[key[i]])
            i += 1

    for i in range(len(buffer)):
        if buffer[i] == ' ':
            new_text += ' '
        elif buffer[i] > 26:
            buffer[i] -= 26

        new_text += ''.join([key for key, valeur in pos_letter.items() if valeur == buffer[i]])

    return new_text


def main():
    pos_letter = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
                  'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                  'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
                  'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                  'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    run = True
    while run:
        key = raw_input('[*] Choisissez une cle : ')
        
        file_path = raw_input('file a utiliser : ')
        with open(file_path, 'r+') as file:
            text = file.read()
            os.remove(file_path)
        
        choice = input('1/ crypt ou 2/ decrypt: ')
        if choice == 1:
            text = encryption(pos_letter, key, text)
            print('Cryptage effectuer')
        elif choice == 2:
            text = decryption(pos_letter, key, text)
            print('decryptage effectuer')
        else:
            run = False

        with open(file_path, 'w') as file:
            file.write(text)


if __name__ == '__main__':
    main()
