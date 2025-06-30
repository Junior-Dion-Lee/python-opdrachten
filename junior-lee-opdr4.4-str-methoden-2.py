__version__ = "0.0.1"
__maintainer__ = " Junior Lee "
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.
#if __name__ == "__main__":
# Hier de hoofdcode

quote = "Het leven is als rijden op een bromfiets. Je moet in beweging blijven om niet om te vallen."
quote2 = 'quote = "Het leven is als rijden op een bromfiets. Je moet in beweging blijven om niet om te vallen."'
quote_fiets = quote.replace("bromfiets", "fiets")
quote_balans = quote.replace("beweging", "balans")
leven = quote.split()[1]
even_letters = quote[::2]
blijven = quote.split("blijven")[1] 
eerste_en_derde = blijven[0] + blijven[2::3]
omgekeerd = quote[::-1]


print(quote2)
print(quote_fiets)
print(quote_balans)
print(quote[2])
print(quote[-2])
print(leven)
print(quote[:9])
print(quote[-13])
print(even_letters)
print(eerste_en_derde)
print(quote[:-8])
print(quote[4:])
print(quote[13:-22])
print(omgekeerd)