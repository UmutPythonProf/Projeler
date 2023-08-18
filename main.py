from random import *
import random

karakterler = "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç1234567890é!'^+%&/()=?_-|\}][{}½$#£><.,:;/*-+]"

x = int(input("Kaç Sembollü Bir Parola İstiyorsun ? =>  "))

for i in range(x):
    y = random.choice(karakterler)
    
    print(y)
    