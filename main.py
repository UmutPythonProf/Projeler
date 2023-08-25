from random import *
import random

karakterler = "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç1234567890é!'^+%&/()=?_-|\}][{}½$#£><.,:;/*-+]"

z = []

x = int(input("Kaç Sembollü Bir Parola İstiyorsun ? =>  "))

def y():
    for i in range(x):
        y = random.choice(karakterler)
    
        print(y)

z.append(x)
