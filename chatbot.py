import re
import random

sapaan = ["Hai juga", "hai juga yang di sana", "Hey to you"]

while True:
    print("\npada kalimat harus terdapat kata halo, hai, atau hey")
    print("sekarang masukkan kalimat")
    x = input("User\t:")
    if re.findall(r'halo|hei|hey', x):
        print("bot\t:"+random.choice(sapaan), "\n")
    else:
        print("bot\t:tidak ada kata sesuai yang dicari dalam kalimat\n")

