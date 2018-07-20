#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from random import randint
from string import maketrans

a_dechiffre = 'fbok fbonbck fteeak yae tkrouadhe à od fkbrktuua qoc da ebdh fte zbddo gbke ya gt zbufcgthcbd'
cle = 't_zya_r_c__gudbfqkehon____'
alphabet="abcdefghijklmnopqrstuvwxyz"

trans = maketrans(cle, alphabet)
dechiffre = a_dechiffre.translate(trans)

print dechiffre




