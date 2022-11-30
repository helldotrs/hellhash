#word+number hellberg-hashgenerator
#copy-left Rebekah Hellberg, @cyberSecHell hellmak.com

#fixme: add year from - year to function :)
#written in ~120min :D

import hashlib


def grab_input():
    print("test/123 for control")

    select  = input("[N]umber or [Y]ear (only use N for now)>>")
    
    if(select=="n"):
        num         = input("number>>") 
        num         = str(num)
    elif(select=="y"):
        year_first  = input("first year>>")
        year_last   = input("last year>>")
        num         = str(year_first)
    else:
        print(":(")
        exit()
    word    = input("word>>") #remove hardcoded values

    #file    = input("filename[.extention]") #add save function
    return word, num

def make_save_file():
    pass

def make_output():
    word, num   = grab_input()
    combos      = make_combos(word, num)
    combos_md5  = make_md5(combos)
    for x, y in zip(combos, combos_md5):
        print(x+":"+y)

    #return make_md5(combos)

    

def make_combos(word, num):
    combo1  = word+num
    combo2  = word.upper()+num
    combo3  = word.lower()+num
    combo4  = word.capitalize()+num

    list    = [combo1,combo2,combo3,combo4]

    return list

def make_md5(plain_list):
    hash_list    =[]
    for item in plain_list:
        hash_list.append(hashlib.md5(item.encode()).hexdigest())
    #return plain_list #fixme - test
    return hash_list


def main_fun():
    #calls all functions
    print(make_output())
    control_text = "test123"
    print(control_text+":"+hashlib.md5(control_text.encode()).hexdigest() + " --> control")
    
    

    

main_fun()
