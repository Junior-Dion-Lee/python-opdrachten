'''Programma schrijft Hallo Python!'''
__author__ = "Junior Lee"
__email__ = "Distrooier2005@gmail.com"
__copyright__ = "Copyright 2024 (C) <Junior Lee >. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = "Junior Lee"
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.
#if __name__ == "__main__":

import random

print("Gok een getal van 1 tot 10")
getal2 = rnd_getal = random.randint(1, 10)


while True:
    getal1 = int(input("?"))

    if getal1 < getal2:
        print(f"Jammer, getal {getal1} is te laag.")
    
    elif getal1 > getal2:
        print(f"Jammer, getal {getal1} is te hoog.")

    else:
        print(f"Gefeliciteerd! Getal {getal1} is goed!")
        print("Tot ziens")
        break