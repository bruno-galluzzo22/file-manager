import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def make_password(password, salt):
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
	)
	return base64.urlsafe_b64encode(kdf.derive(password))

def do_criptography(criptography,password):
    password = bytes(password,'utf-8')
    criptography = bytes(criptography,'utf-8')
    salt = os.urandom(16)
    cipher_suite = Fernet(make_password(password, salt))
    return base64.b64encode(salt).decode('utf-8') +  cipher_suite.encrypt(criptography).decode('utf-8')

def do_decriptography(file,password):
    try:
        _password=bytes(password,'utf-8')
        salt = base64.b64decode(file[:24].encode("utf-8"))
        cipher_suite = Fernet(make_password(_password, salt))
        _password=bytes(file[24:],'utf-8')
        return cipher_suite.decrypt(_password).decode('utf-8')
    except:
       pass 
