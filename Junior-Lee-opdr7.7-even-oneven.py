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

getallen = "12,3,7,25,771,45,6,98,55,546"

getallen_lijst = getallen.split(",")

for getal in getallen_lijst:
    getal_int = int(getal)
    if getal_int % 2 == 0:
        print(f"{getal_int} is even")

    else:
        print(f"{getal_int} is oneven")