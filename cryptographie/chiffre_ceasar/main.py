#! /usr/bin/python
# -*- coding:utf-8 -*-
import os

global key

old_key = 'abcdefghijklmno pqrstuvwxyz\'\"!:;.,?ABCDEFGHIJKLM\nNOPQRSTUVWXYZ'
key = 'abcdefghijklmnopqrstuvwxyz'
run = True


def encryption(decrypted):
    encrypted_string = ''
    for letter in decrypted:
        if letter in key:
            index = key.index(letter)
            index += 2
            if index > 25:
                index -= 26
            encrypted_string += key[index]
        else:
            encrypted_string = encrypted_string + letter
    return encrypted_string


def decryption(encrypted_string):
    decrypted = ''
    for letter in encrypted_string:
        if letter in key:
            index = key.index(letter)
            index -= 2
            if index < 0:
                index += 26
            decrypted += key[index]
        else:
            decrypted = decrypted + letter
    return decrypted


def file():
    print('[*] Choisir de crypter ou de decrypter un fichier :')
    choice = input('1/ crypt\n2/ decrypt\n')

    if choice == 1:
        file_path = raw_input('[*] Fichier a chiffrer :')
        with open(file_path, 'r+') as file:
            decrypted = file.read()
            encrypted_string = encryption(decrypted)

        os.remove(file_path)
        file_path = path_test(file_path)

        with open('crypt_'+file_path, 'w') as new_file:
            new_file.write(encrypted_string)

    elif choice == 2:
        file_path = raw_input('[*] Fichier a decrypted :')
        with open(file_path, 'r+') as file:
            encrypted_string = file.read()
            decrypted = decryption(encrypted_string)

        os.remove(file_path)
        file_path = path_test(file_path)

        with open('decrypt_'+file_path, 'w') as new_file:
            new_file.write(decrypted)

    os.system('clear')


def string():
    print('[*] Choisir de chiffrer ou de dechiffrer une chaine :')
    choice = input('1/ crypt\n2/ decrypt\n')

    if choice == 1:
        print('[*] Chaine à chiffrer : ')
        string = raw_input()
        print(encryption(string))
    elif choice == 2:
        print('[*] Chaine à déchiffrer : ')
        string = raw_input()
        print(decryption(string))


def path_test(path):
    if path[:6] == 'crypt_':
        path = path[6:]
    elif path[:8] == 'decrypt_':
        path = path[8:]
    return path

while run:
    print('[*] Choisir de travailler sur un fichier ou une chaine :')
    try:
        choice = input('1/ fichier\n2/ chaine\n')
    except Exception:
        break

    if choice == 1:
        file()
    elif choice == 2:
        string()
    else:
        pass
