#word+number hellberg-hashgenerator
#copy-left Rebekah Hellberg, @cyberSecHell hellmak.com

import hashlib


def grab_input():
    word    = input("word>") #remove hardcoded values
    num     = input("number>")   
    #file    = input("filename[.extention]") #add save function
    return word, num

def make_save_file():
    pass

def make_output():
    word, num   = grab_input()
    return make_md5(word + num)

def make_md5(x):
    return hashlib.md5(x.encode()).hexdigest()



def main_fun():
    #calls all functions
    print(make_output())
    print(hashlib.md5("test123".encode()).hexdigest())
    
    

    

main_fun()
