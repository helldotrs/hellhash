#word+number hellberg-hashgenerator
#copy-left Rebekah Hellberg, @cyberSecHell hellmak.com

import hashlib


def grab_input():
    print("test/123 for control")
    word    = input("word>") #remove hardcoded values
    num     = str(input("number>")) #str(input("number>")) gives different output   
    #file    = input("filename[.extention]") #add save function
    return word, num

def make_save_file():
    pass

def make_output():
    word, num   = grab_input()
    return make_md5(word + num)

def make_combos(word, num):
    combo1  = word+num

def make_md5(x):
    return hashlib.md5(x.encode()).hexdigest()



def main_fun():
    #calls all functions
    print(make_output())
    print(hashlib.md5("test123".encode()).hexdigest() + " --> control")
    
    

    

main_fun()
