from zipfile import ZipFile
import zlib

with open('SecLists/Passwords/Leaked-Databases/Ashley-Madison.txt', "r", encoding='latin-1') as f:
    passwords = [line.strip() for line in f]

with ZipFile('whitehouse_secrets.zip') as zf: 
    for i,password in enumerate(passwords):
        if i%1000==0:
            print('i=',i,'password=',password)
        with ZipFile('whitehouse_secrets.zip') as zf:
            try:
                zf.extractall(pwd=password.encode('latin-1'))
                zf.extractall(pwd=password.encode('ascii'))
                print('password=', password)
                break
            except (RuntimeError, zlib.error):
                pass

