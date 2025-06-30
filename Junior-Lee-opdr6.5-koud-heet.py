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

print("wat is de tempratuur in °C ?")
temp = int(print("?"))

if temp < 0:
    print("het is koud!")

elif temp >= 0 and temp <= 10:
    print("het is fris!")

elif temp >= 11 and temp <= 17:
    print("het is koel!")

elif temp >= 18 and temp <= 24:
    print("het is lekker weer!")

elif temp >= 25 and temp <= 31:
    print("het is warm!")

elif temp >= 32 and temp <= 40:
    print("het is warm!")

elif temp > 40:
    print("het is heet!")


