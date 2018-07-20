#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from random import randint
from string import maketrans

if (len(sys.argv)>1):
    # Normal alphabet
    alphabet="abcdefghijklmnopqrstuvwxyz"

    # Randomly create a new cipherbet
    cipherbet=""
    left=alphabet
    for i in range(0,len(alphabet)):
        x=randint(0,len(left)-1)
        cipherbet+=left[x]
        left=left[:x]+left[x+1:]

    # Get input text to translate
    text=sys.argv[1].lower()

    trantab = maketrans(alphabet,cipherbet)
    text=text.translate(trantab)

    # Replace unused letters in cipherbet with _'s
    for i in cipherbet:
        if i not in text:
            cipherbet=cipherbet.replace(i,"_")

    # Print cipherbet (solution) and the text (cryptogram)
    print cipherbet
    print text