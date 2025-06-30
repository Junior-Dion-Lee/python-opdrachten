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

temp = ( 22.7, 30.8, 26.8, 19.3, 16.7, 38.9, 32.5, 27.5, 24.5 )
print(max(temp))
print(min(temp))
print(len(temp))

product = 1
for num in temp:
    product *= num
print(product)

new_tuple = temp[2:6]
print(new_tuple)

