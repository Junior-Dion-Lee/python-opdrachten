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

vakkenlijst = [ 'JavaScript', 'Python', 'HTML', 'CSS', 'LiveScript', 'PHP',
'EcmaScript' ]

print(vakkenlijst)
print(len(vakkenlijst))
print(vakkenlijst[1])

vakkenlijst.sort()
print(vakkenlijst)
vakkenlijst.remove('LiveScript')
print(vakkenlijst)
vakkenlijst.remove('PHP')
print(vakkenlijst)

index = vakkenlijst.index('EcmaScript')
vakkenlijst[index] = 'ES6'
print(vakkenlijst)

vakkenlijst = vakkenlijst[:2] + vakkenlijst[4:]
print(vakkenlijst)

vakkenlijst = [vak.lower() for vak in vakkenlijst]
print(vakkenlijst)