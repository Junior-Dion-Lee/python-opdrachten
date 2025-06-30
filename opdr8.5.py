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

import pprint # Importeren van de library pretty print

fav_boek = {
"titel" : "Guns, germs and steel",
"subtitel" : "The Fates of Human Societies",
"schrijver" : "Jared Diamond",
"jaar" : 2007,
"uitgever" : "Ww Norton & Co"
}

fav_boek["jaar"] = fav_boek["jaar"] - 10 
print(fav_boek)

fav_boek["ISBN"] = "0-393-03891-2"
print(fav_boek)

del fav_boek["subtitel"]
print(fav_boek)

print(fav_boek["schrijver"])

fav_boek = {
"titel" : "Guns, germs and steel",
"subtitel" : "The Fates of Human Societies",
"schrijver" : "Jared Diamond",
"jaar" : 2007,
"uitgever" : "Ww Norton & Co"
}
pprint.pprint(fav_boek) # Print de dictionary fav_boek netjes naar het scherm

