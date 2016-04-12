#!/usr/bin/python
# Creado by n0ipr0cs

import getpass
import hashlib
import sys

print ""
print "	/ )( \ / _\ / ___)/ )( \/ ___)(  __) / _\ ( \/ )(  __)"
print "	) __ (/    \\___ \) __ (\___ \ ) _) /    \/ \/ \ ) _)" 
print "	\_)(_/\_/\_/(____/\_)(_/(____/(____)\_/\_/\_)(_/(____)"
print "***********************by n0ipr0cs***************************"

#creacion de las funciones de los hash
def MD5_HASH():
	passwd = getpass.getpass()
	HASH_MD5 = hashlib.md5(passwd).hexdigest()
	print HASH_MD5
	return
def SHA1_HASH():
	passwd = getpass.getpass()
	HASH_MD5 = hashlib.sha1(passwd).hexdigest()
	print HASH_MD5
	return
def SHA256_HASH():
	passwd = getpass.getpass()
	HASH_MD5 = hashlib.sha256(passwd).hexdigest()
	print HASH_MD5
	return
def SHA512_HASH():
	passwd = getpass.getpass()
	HASH_MD5 = hashlib.sha512(passwd).hexdigest()
	print HASH_MD5
	return




print " 1 .md5"
print " 2 .sha1"
print " 3 .sha256"
print " 4 .sha512"

VAR_1 = raw_input("Elige un algoritmo para tu password")

if VAR_1 == "1":
	MD5_HASH()
elif VAR_1 == "2":
	SHA1_HASH()
elif VAR_1 == "3":
	SHA256_HASH()
elif VAR_1 == "4":
	SHA512_HASH()
else:
	print "ERROR!!!  Elige una opcion valida"
sys.exit(1)



sys.exit(0)
