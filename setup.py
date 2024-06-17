#--[ CODE BY - @BD_Hacker99 ]
#--[ JOIN _ @Hacker_999_BD ]

import os,sys,string
try:import zipfile
except:os.system('pip install zipfile')
try:import hashlib
except:os.system('pip install hashlib')
try:import itertools
except:os.system('pip install itertools')

def NJxFORCE(file_path, password):
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        password_nahid=nahid.sha256(password.encode()).hexdigest()
        zip_file.setpassword(password.encode())
        if zip_file.testzip():
            print(f"Password Found : {password}")
        else:
            print(f"Password Wrong : {password}")

def NJx99():
    file_path=input("\n<+/ Target Zip Path : ")
    password=input("\n</> Press Enter To Attack ! ")
    if password:
        NJxFORCE(file_path, password)
    else:
        lmnXpTs=input("\n<+/ PassList Path : ")
        with open(lmnXpTs, 'r') as f:
            passwords=[line.strip() for line in f.readlines()]
        for password in itertools.permutations(passwords):
            NJxFORCE(file_path, ''.join(password))
            
chnl="https://t.me/Hacker_999_BD"
if __name__ in '__main__':
    os.system(f'xdg-open {chnl}')
    NJx99()