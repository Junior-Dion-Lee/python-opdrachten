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

def kenmerk_string(str):  
    print(str)  
    aantal_karakters = len(str)  
    print(aantal_karakters)
    woorden = str.split()  
    aantal_woorden = len(woorden) 
    print(aantal_woorden)
    totaal_karakters = sum(len(woord) for woord in woorden)  # Tel het aantal karakters
    gemiddeld = totaal_karakters / aantal_woorden 

    
    return aantal_karakters, aantal_woorden, gemiddeld # Return values

# Get input and store the returned values
aantal_karakters, aantal_woorden, gemiddeld  = kenmerk_string(input("Voer een string in: "))

# Now print the returned values
print(f"Opgeslagen waarden - Karakters: {aantal_karakters}, Woorden: {aantal_woorden}, Gemidelde lengte per word: {gemiddeld:.1f}")


