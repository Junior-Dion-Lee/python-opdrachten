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


movies = [
 { "titel" : "The Godfather",
 "jaar" : 1972,
 "cijfer" : 9.2,
 "regisseur" : "Francis Ford Coppola" },
 { "titel" : "The Shawshank Redemption",
 "jaar" : 1994,
 "cijfer" : 9.3,
 "regisseur" : "Frank Darabont" },
 { "titel" : "Schindler's List",
 "jaar" : 1993,
 "cijfer" : 8.9,
 "regisseur" : "Steven Spielberg" },
 { "titel" : "Raging Bull",
 "jaar" : 1980,
 "cijfer" : 8.2,
 "regisseur" : "Martin Scorsese" },
 { "titel" : "Casablanca",
 "jaar" : 1942,
 "cijfer" : 8.5,
 "regisseur" : "Michael Curtiz" }
]

import pprint # Importeren van de library pretty print
for movie in movies:
    print(movie["titel"])
    if movie["jaar"] < 1990:
        print(movie["jaar"])

for movie in movies:
    if movie["regisseur"] == "Steven Spielberg":  # Vergelijking met een string
        pprint.pprint(movie)



max_cijfer = max(movie["cijfer"] for movie in movies)  # Zoek hoogste cijfer
for movie in movies:
    if movie["cijfer"] == max_cijfer:  # Vergelijk de cijfers
        print(movie["titel"])
        print(movie["cijfer"])
        
print("---")

movies_sorted = sorted(movies, key=lambda movie: movie["jaar"])  # Sorteer op jaar

for movie in movies_sorted:
    print(movie)