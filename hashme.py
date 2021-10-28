#!/usr/bin/env python
#coding: utf-8
#AUTHOR : DEVIL MASTER

import hashlib
from base64 import b64encode, b64decode
import codecs
import binascii
import re
from time import sleep
import sys
from platform import python_version
from art import *
from os import system, name
from Crypto.Hash import MD2
import pycryptodome

########################### BEGIN ###########################

def author():
	print("   \033[37m[\033[31m|\033[37m]|------------------------------------------------|\033[37m[\033[31m|\033[37m]")
	print("   \033[37m[\033[31m|\033[37m]|          DEVELOPED BY DEVIL MASTER             |\033[37m[\033[31m|\033[37m]")
	print("   \033[37m[\033[31m|\033[37m]|              github.com/isuruwa                |\033[37m[\033[31m|\033[37m]")
	print("   \033[37m[\033[31m|\033[37m]|------------------------------------------------|\033[37m[\033[31m|\033[37m]\n")

if sys.version_info[0] < 3:
    versao = python_version()
    print(
        "\n\033[32m You are using python in the version\033[1;m \033[1m\033[31m%s\033[1;m \033[32mand it is lower than python3 onwards.\033[1;m"
        % (versao))
    print(
        "\033[32m Please run HashCode with a higher version than python2\033[1;m\n"
    )
    exit(1)

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def banner(topic):
    clear()
    print("\033[1;32m")
    tprint(topic)
    author()


def re(reb, again):
	rec = input(reb)
	if rec == "y" or rec == "Y":
		again()
	elif rec == "n" or rec == "N":
		menu()
	else:
		re(reb,again)

########################### MENU ###########################

def menu():
    banner("""       HASHME\n""")
    print("\033[35m  [\033[37m1\033[35m]\033[37m  ENCODE MD2")
    print("\033[35m  [\033[37m2\033[35m]\033[36m  ENCODE MD4")
    print("\033[35m  [\033[37m3\033[35m]\033[1;32m  Encode MD5")
    print("\033[35m  [\033[37m4\033[35m]\033[34m  Encode SHA1")
    print("\033[35m  [\033[37m5\033[35m]\033[35m  Encode SHA224")
    print("\033[35m  [\033[37m6\033[35m]\033[36m  ENCODE SHA256")
    print("\033[35m  [\033[37m7\033[35m]\033[37m  ENCODE SHA384")
    print("\033[35m  [\033[37m8\033[35m]\033[1;32m  ENCODE SHA512")
    print("\033[35m  [\033[37m9\033[35m]\033[37m  ENCODE SHA3-224")
    print("\033[35m  [\033[37m10\033[35m]\033[36m  ENCODE SHA3-256")
    print("\033[35m  [\033[37m11\033[35m]\033[37m  ENCODE SHA3-512")
    print("\033[35m  [\033[37m12\033[35m]\033[37m  ENCODE|DECODE BASE32")
    print("\033[35m  [\033[37m13\033[35m]\033[31m  ENCODE|DECODE BASE58")
    print("\033[35m  [\033[37m14\033[35m]\033[31m  ENCODE|DECODE BASE64")
    print("\033[35m  [\033[37m15\033[35m]\033[35m  ENCODE|DECODE BINARY")
    print("\033[35m  [\033[37m16\033[35m]\033[36m  ENCODE|DECODE CIPHER OF CESAR")
    print("\033[35m  [\033[37m17\033[35m]\033[31m  ENCODE|DECODE HEXADECIMAL")
    print("\033[35m  [\033[37m18\033[35m]\033[1;32m  ENCODE|DECODE REVERSE\n")

    choice = input("\033[37m  [\033[31m+\033[37m] Enter Choice : ")
    if choice == "1" or choice == "01":
      md2()
    elif choice == "2" or choice == "02":
      md4()
    elif choice == "3" or choice == "03":
      md5()
    elif choice == "4" or choice == "04":
      sha1()
    elif choice == "5" or choice == "05":
      sha224()
    elif choice == "6" or choice == "06":
      sha256()
    elif choice == "7" or choice == "07":
      sha384()
    elif choice == "8" or choice == "08":
      sha512()
    elif choice == "9" or choice == "09":
      sha3224()
    elif choice == "10":
      sha3256()
    elif choice == "11":
      sha3512()
    elif choice == "12":
      base32()
    elif choice == "13":
      base58()
    elif choice == "14":
      base64()
    elif choice == "15":
        binary()
    elif choice == "16":
        coc()
    elif choice == "17":
        hexa()
    elif choice == "18":
        reverse()
    elif choice == "":
        menu()
    else:
      print("\033[37m  [\033[31m+\033[37m] WRONG CHOICE")
      sleep(2)
      menu()

########################### MD5 ###########################

def md5():
    banner("""MD5""")
    text = input("\033[1;32m [+] Text To Encrypt In MD5 : ")
    hash = hashlib.md5(text.encode())
    print("\n")
    print("\033[1;32m [+] Result : " + hash.hexdigest())
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ",md5)


########################### SHA1 ###########################

def sha1():
    banner("""SHA1""")
    text = input("\033[1;32m [+] Text To Encrypt In SHA1 : ")
    hash = hashlib.sha1(text.encode())
    print("\n")
    print("\033[1;32m [+] Result : " + hash.hexdigest())
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", sha1)

########################### SHA224 ###########################

def sha224():
    banner("""SHA224""")
    text = input("\033[1;32m [+] Text To Encrypt In SHA224 : ")
    hash = hashlib.sha224(text.encode())
    print("\n")
    print("\033[1;32m [+]  : " + hash.hexdigest())
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", sha224)
    

########################### SHA256 ###########################

def sha256():
    banner("""SHA256""")
    text = input("\033[1;32m [+] Text To Encrypt In SHA256 : ")
    hash = hashlib.sha256(text.encode())
    print("\n")
    print("\033[1;32m [+] Result : " + hash.hexdigest())
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", sha256)
    

########################### SHA384 ###########################

def sha384():
    banner("""SHA384""")
    text = input("\033[1;32m [+] Text To Encrypt In SHA384 : ")
    hash = hashlib.sha384(text.encode())
    print("\n")
    print("\033[1;32m [+] Result : " + hash.hexdigest())
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", sha384)
    

########################### SHA512 ###########################

def sha512():
    banner("""SHA512""")
    text = input("\033[1;32m [+] Text To Encrypt In SHA512 : ")
    hash = hashlib.sha512(text.encode())
    print("\n")
    print("\033[1;32m [+] Result : " + hash.hexdigest())
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", sha512)

########################### BASE64 ###########################

def base64():
    banner("""BASE64""")
    print("\033[1;32m [+] Choose a Option : \n")
    print("\033[1;32m [1] BASE64 - ENCODE ")
    print("\033[1;32m [2] BASE64 - DECODE \n")
    option = input("\033[37m [+] Enter Option : ")
    if option == "1" or option == "01":
        base64encode()
    if option == "2" or option == "02":
        base64decode()
    else:
        base64()


def base64encode():
    banner("""BASE64""")
    text = input("\033[1;32m [+] Text To  BASE64 : ")
    b64e = b64encode(text.encode('utf-8'))
    b64d = b64e.decode('utf-8')
    print("\n")
    print("\033[1;32m [+] Result : " + b64d)
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", base64encode)


def base64decode():
    banner("""BASE64""")
    text = input("\033[1;32m [+] BASE64 TO TEXT : ")
    try:
        b64d = b64decode(text).decode('utf-8')
        print("\n")
        print("\033[1;32m [+] Result : " + b64d)
        print("\n")
        re("\033[31m [+] Do a another decode (y/n) ? ", base64decode)
    except:
        print("\033[1;32m [+] Incorrect Padding")
        print("\n")
        time.sleep(2)
        base64decode()
        

########################### BINARY ###########################


def binary():
    banner("""BINARY""")
    print("\033[1;32m [+] Choose a Option : \n")
    print("\033[1;32m [1] BINARY - ENCODE ")
    print("\033[1;32m [2] BINARY - DECODE \n")
    option = input("\033[37m [+] Enter Option : ")
    if option == "1" or option == "01":
        binaryencode()
    if option == "2" or option == "02":
        binarydecode()
    else:
        binary()


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def binarydecode(encoding='utf-8', errors='surrogatepass'):
    banner("""BINARY""")
    try:
        text = input("\033[1;32m [+] BINARY TO TEXT : ")
        hash = text.replace(" ", "")
        bi = int(hash, 2)
        print("\n")
        print("\033[1;32m [+] Result : " + int2bytes(bi).decode(encoding, errors))
        print("\n")
        re("\033[31m [+] Do a another decode (y/n) ? ", binarydecode)
    except:
        print("\033[1;32m [+] Error Value")
        print("\n")
        sleep(2)
        binarydecode()


def binaryencode(encoding='utf-8', errors='surrogatepass'):
    banner("""BINARY""")
    try:
        text = input("\033[1;32m [+] BINARY TO TEXT : ")
        bits = bin(int(binascii.hexlify(text.encode(encoding, errors)),
                       16))[2:]
        print("\n")
        print("\033[1;32m [+] Result : " + bits.zfill(8 * ((len(bits) + 7) // 8)))
        print("\n")
        re("\033[31m [+] Do a another encode (y/n) ? ", base64encode)
    except:
        print("\033[1;32m [+] Error Value")
        print("\n")
        sleep(2)
        binaryencode()

        
########################### HEXADECIMAL ###########################


def hexa():
    banner("""HEXADECIMAL""")
    print("\033[1;32m [+] Choose a Option : \n")
    print("\033[1;32m [1] HEXADECIMAL - ENCODE")
    print("\033[1;32m [2] HEXADECIMAL - DECODE \n")
    option = input("\033[37m [+] Enter Option : ")
    if option == "1" or option == "01":
        hexaencode()
    if option == "2" or option == "02":
        hexadecode()


def hexaencode():
    text = input("\033[1;32m [+] TEXT TO HEXADECIMAL")
    print("")
    encode = binascii.hexlify(bytes(text, "utf-8"))
    encode = str(encode).strip("b")
    encode = encode.strip("'")
    encode = re.sub(r'(..)', r'\1 ', encode).strip()
    print("\n")
    print("\033[1;32m [+] Result : " + encode)
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", hexaencode)


def hexadecode():
    try:
        text = input("\033[1;32m [+] HEXADECIAML TO TEXT : ")
        print("")
        decode = bytes.fromhex(text).decode('utf-8')
        print("\n")
        print("\033[1;32m [+] Result : " + decode)
        print("\n")
        re("\033[31m [+] Do a another decode (y/n) ? ", hexadecode)
    except:
        print("Error Value")
        print("\n")
        sleep(2)
        hexadecode()

        
########################### CIPHER OF CESAR ###########################

def coc():
    banner("""CIPHER OF CESAR""")
    print("\033[1;32m [+] Choose a Option : \n")
    print("\033[1;32m [1] CIPHER OF CESAR - ENCODE ")
    print("\033[1;32m [2] CIPHER OF CESAR - DECODE \n")
    option = input("\033[37m [+] Enter Option : ")
    if option == "1" or option == "01":
        cocencode()
    if option == "2" or option == "02":
        cocdecode()


def cifrar(palavras, chave):
    abc = "abcdefghijklmnopqrstuvwxyz "
    text_cifrado = ''

    for letra in palavras:
        soma = abc.find(letra) + chave
        modulo = int(soma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])

    return text_cifrado


def decifrar(palavras, chave):
    abc = "abcdefghijklmnopqrstuvwxyz "
    text_cifrado = ''

    for letra in palavras:
        soma = abc.find(letra) - chave
        modulo = int(soma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])

    return text_cifrado


def cocencode():
    banner("""CIPHER OF CESAR""")
    try:
        text = str(input("\033[1;32m [+] TEXT TO CIPHER: ")).lower()
        key = int(input("\033[1;32m [+] ENTER KEY : "))
        print("\n")
        print("\033[1;32m [+] RESULT : ", cifrar(text, key))
        print("\n")
        re("\033[31m [+] Do a another encode (y/n) ? ", cocencode)
    except:
        print("VALUE ERROR")
        print("\n")
        time.sleep(2)
        cocencode()


def cocdecode():
    banner("""CIPHER OF CESAR""")
    try:
        text = str(input("\033[1;32m [+] CYPHER TO TEXT : ")).lower()
        key = int(input("\033[1;32m [+] ENTER KEY : "))
        print("\n")
        print("\033[1;32m [+] RESULT : ", decifrar(text, key))
        print("\n")
        re("\033[31m [+] Do a another decode (y/n) ? ", cocdecode)
    except:
        print("VALUE ERROR")
        print("\n")
        time.sleep(2)
        cocdecode()

 ################## md2 ######################

def md2():
  banner("""MD2""")
  text = str(input("\033[1;32m [+] TEXT TO MD2 : "))
  hashObject = MD2.new()
  hashObject.update(text.encode('utf-8'))
  digest = hashObject.hexdigest()
  print("\033[1;32m [+] RESULT : " , (digest))
  print("\n")
  re("\033[31m [+] Do a another decode (y/n) ? ", cocdecode)

############## md4 ##############################

def md4():
  banner("""MD4""")
  text = str(input("\033[1;32m [+] TEXT TO MD2 : "))
  hashObject = MD4.new()
  hashObject.update(text.encode('utf-8'))
  digest = hashObject.hexdigest()
  print("\033[1;32m [+] RESULT : " , (digest))
  print("\n")
  re("\033[31m [+] Do a another decode (y/n) ? ", cocdecode)

##################### sha3-224 ################################
def sha3224():
  banner("""SHA3-224""")
  text = str(input("\033[1;32m [+] TEXT TO SHA-224 : "))
  hashObject = hashlib.sha3_224(text.encode('utf-8'))
  digest = hashObject.hexdigest()
  print("\033[1;32m [+] RESULT : " , (digest))
  print("\n")
  re("\033[31m [+] Do a another decode (y/n) ? ", cocdecode)

##################### sha3-256 ################################
def sha3256():
  banner("""SHA3-256""")
  text = str(input("\033[1;32m [+] TEXT TO SHA-256 : "))
  hashObject = hashlib.sha3_256(text.encode('utf-8'))
  digest = hashObject.hexdigest()
  print("\033[1;32m [+] RESULT : " , (digest))
  print("\n")
  re("\033[31m [+] Do a another decode (y/n) ? ", cocdecode)

##################### sha3-384 ################################
def sha3384():
  banner("""SHA3-384""")
  text = str(input("\033[1;32m [+] TEXT TO SHA-384 : "))
  hashObject = hashlib.sha3_384(text.encode('utf-8'))
  digest = hashObject.hexdigest()
  print("\033[1;32m [+] RESULT : " , (digest))
  print("\n")
  re("\033[31m [+] Do a another decode (y/n) ? ", cocdecode)

##################### sha3-512 ################################
def sha3512():
  banner("""SHA3-512""")
  text = str(input("\033[1;32m [+] TEXT TO SHA-384 : "))
  hashObject = hashlib.sha3_512(text.encode('utf-8'))
  digest = hashObject.hexdigest()
  print("\033[1;32m [+] RESULT : " , (digest))
  print("\n")
  re("\033[31m [+] Do a another decode (y/n) ? ", cocdecode)

#################### base32 ############################

def base32():
    banner("""BASE64""")
    print("\033[1;32m [+] Choose a Option : \n")
    print("\033[1;32m [1] BASE32 - ENCODE ")
    print("\033[1;32m [2] BASE32 - DECODE \n")
    option = input("\033[37m [+] Enter Option : ")
    if option == "1" or option == "01":
        base32encode()
    if option == "2" or option == "02":
        base32decode()
    else:
        base32()


def base32encode():
    banner("""BASE64""")
    text = input("\033[1;32m [+] Text To  BASE64 : ")
    b32e = base64.b32encode(text.encode('utf-8')).decode('utf-8')
    print("\n")
    print("\033[1;32m [+] Result : " + b32e)
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", base32encode)


def base32decode():
    banner("""BASE32""")
    text = input("\033[1;32m [+] BASE32 TO TEXT : ")
    try:
        b32d = base64.b32decode(base32Str).decode('utf-8')
        print("\n")
        print("\033[1;32m [+] Result : " + b32d)
        print("\n")
        re("\033[31m [+] Do a another decode (y/n) ? ", base32decode)
    except:
        print("\033[1;32m [+] Incorrect Padding")
        print("\n")
        time.sleep(2)
        base32decode()

#################### base32 ############################

def base58():
    banner("""BASE58""")
    print("\033[1;32m [+] Choose a Option : \n")
    print("\033[1;32m [1] BASE58 - ENCODE ")
    print("\033[1;32m [2] BASE58 - DECODE \n")
    option = input("\033[37m [+] Enter Option : ")
    if option == "1" or option == "01":
        base58encode()
    if option == "2" or option == "02":
        base58decode()
    else:
        base58()


def base58encode():
    banner("""BASE58""")
    text = input("\033[1;32m [+] Text To  BASE58 : ")
    base58s = base58.b58encode(text.encode('utf-8')).decode('utf-8')
    print("\n")
    print("\033[1;32m [+] Result : " + base58s)
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", base58encode)


def base58decode():
    banner("""BASE58""")
    text = input("\033[1;32m [+] BASE58 TO TEXT : ")
    try:
        base58d = base58.b58decode(base58Str).decode('utf-8')
        print("\n")
        print("\033[1;32m [+] Result : " + b32d)
        print("\n")
        re("\033[31m [+] Do a another decode (y/n) ? ", base58decode)
    except:
        print("\033[1;32m [+] Incorrect Padding")
        print("\n")
        time.sleep(2)
        base58decode()


########################### REVERSE ###########################


def reverse():
    banner("""REVERSE""")
    print("\033[1;32m [+] Choose a Option : \n")
    print("\033[1;32m [1] REVERSE TEXT - ENCODE")
    print("\033[1;32m [2] REVERSE TEXT - DECODE \n")
    option = input("\033[37m [+] Enter Option : ")
    if option == "1" or option == "01":
        revencode()
    if option == "2" or option == "02":
        revdecode()


def revencode():
    banner("""REVERSE""")
    text = input("\033[1;32m [+] TEXT TO REVERSE : ")
    print("\n")
    print("\033[1;32m [+] Result : " + text[::-1])
    print("\n")
    re("\033[31m [+] Do a another encode (y/n) ? ", revencode)


def revdecode():
    banner("""REVERSE""")
    text = input("\033[1;32m [+] REVERSE TO TEXT : ")
    print("\n")
    print("\033[1;32m [+] Result : " + text[::-1])
    print("\n")
    re("\033[31m [+] Do a another decode (y/n) ? ", revdecode)

def program():
    try:
      menu()
    except KeyboardInterrupt:
      con = input("\n\n\033[31m  [c] Continue [q] Quit : ")
      if con == "c" or con == "C" or con == "continue" or con == "Continue":
        menu()
      else:
        exit()
	
if '__main__' == __name__:
	program()
