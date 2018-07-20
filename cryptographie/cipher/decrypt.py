#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
from random import randint
from string import maketrans

crypted_data = 'fbok fbonbck fteeak yae tkrouadhe à od fkbrktuua qoc da ebdh fte zbddo gbke ya gt zbufcgthcbd'
key = 't_zya_r_c__gudbfqkehon____'
alphabet="abcdefghijklmnopqrstuvwxyz"

trans = maketrans(key, alphabet)
decrypted = crypted_data.translate(trans)

print decrypted
