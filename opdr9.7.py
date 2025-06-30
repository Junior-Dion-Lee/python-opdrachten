#'''Programma schrijft Hallo Python!'''
#__author__ = "Junior Lee"
#__email__ = "Distrooier2005@gmail.com"
#__copyright__ = "Copyright 2024 (C) <Junior Lee >. All rights reserved."
#__license__ = "GNU General Public License v2.0"
#__version__ = "0.0.1"
#__maintainer__ = "Junior Lee"
#__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.
#if __name__ == "__main__":

import math

def formule_berekenen():
    print("Gegeven de volgende tweedegraadsfunctie:")
    print("y = ax² + bx + c") 
    
    
    a = float(input("Geef waarde voor A: "))
    b = float(input("Geef waarde voor B: "))
    c = float(input("Geef waarde voor C: "))

    
    d = b**2 - 4 * a * c

    
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
    else:
        x1 = x2 = None  # Geen reële oplossingen

    x = (x1 + x2) / 2 if d >= 0 else None

    print(f"De ingevulde functie is: y = {a}x² + {b}x + {c}")

    if d > 0:
        print(f"De functie heeft 2 nulpunten: x1 = {x1}, x2 = {x2}")
    elif d == 0:
        print(f"De functie heeft 1 nulpunt: x = {x1}")
    else:
        print("De functie heeft geen nulpunten (D < 0)")

   
    if a > 0:
        print(f"De functie is een dalparabool met x, y positie ({x}, {c})")
    else:
        print(f"De functie is een bergparabool met x, y positie ({x}, {c})")

    return x1, x2, d


formule_berekenen()