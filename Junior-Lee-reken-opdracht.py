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


print("kies uit +, -, *, /.")
Reken_Teken = str(input("?"))
print("geef een (geheel) getal")
Getal1 = int(input("?"))
print("geef een (geheel) getal")
Getal2 = int(input("?"))

p = Getal1 + Getal2 #voor +
m = Getal1 - Getal2 #voor -
k = Getal1 * Getal2 #voor *
g = Getal1 / Getal2 if Getal1 and Getal2 != "Is niet mogenlijk" else "Is niet mogenlijk"
#voor / en zodat 0/0 niet kan


uitkomst = Reken_Teken

if Reken_Teken == "+":  
    Reken_Teken = p # zodat het symbol gebruikt kan worden om te reken
    print(f"Resultaat van {Getal1} {uitkomst} {Getal2} is {p}")

elif Reken_Teken == "-": 
    Reken_Teken = m # zodat het symbol gebruikt kan worden om te reken
    print(f"Resultaat van {Getal1} {uitkomst} {Getal2} is {m}")

elif Reken_Teken == "*": 
    Reken_Teken = k # zodat het symbol gebruikt kan worden om te reken
    print(f"Resultaat van {Getal1} {uitkomst} {Getal2} is {k}")

elif Reken_Teken == "/": 
    Reken_Teken = g # zodat het symbol gebruikt kan worden om te reken
    print(f"Resultaat van {Getal1} {uitkomst} {Getal2} is {g}")




