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


n = 250
som = 0

while n <= 500:
    som += n

    print(f"getal {n} som {som} kwadraat {n**2}")
    n += 1

aantal_getallen = 500 - 250 + 1 
gemiddelde = som / aantal_getallen
print(f"gemiddelde {gemiddelde}")