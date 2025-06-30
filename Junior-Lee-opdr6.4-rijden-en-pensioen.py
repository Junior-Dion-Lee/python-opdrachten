'''Programma schrijft code'''
__author__ = "Junior Lee"
__email__ = "juniorlee7847@gmail.com"
__copyright__ = "Copyright 2024 (C) < Junior Lee >. All rights reserved."
__license__ = "GNU General Public License v2.0"
__version__ = "0.0.1"
__maintainer__ = " Junior Lee "
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.
#if __name__ == "__main__":
# Hier de hoofdcode 

print("Wat is uw leeftijd?")
jaar = int(input("?"))
if jaar >= 18 and jaar < 68:
    print("Je mag autorijden maar nog niet met pensioen !")

elif jaar <= 18:
    print("Je bent te jong om auto te rijden !")

elif jaar >= 68:
    print("je mag autorijden en met pensioen gaan !")

elif jaar >= 120:
    print(f"uw leeftijd is {jaar}")
    print("geef een geldige leeftijd op !")
    
