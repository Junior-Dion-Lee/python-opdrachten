__version__ = "0.0.1"
__maintainer__ = " Junior Lee "
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.
#if __name__ == "__main__":
# Hier de hoofdcode


quote = ' Eet vriend en vriendin en wordt dronken van liefde. '
quote2 = "' Eet vriend en vriendin en wordt dronken van liefde. '"
quote_strip = quote.strip() 
quote_up = quote.upper()
quote_title = quote.title()
quote_len = quote.__len__()
quote_start = quote.startswith("e")
quote_ends = quote.endswith("l")
quote_cnt_d = quote.count("d")
quote_cnt_z = quote.count("z")


print(quote2)
print(quote_strip)
print(quote_up)
print(quote_title)
print(quote)
print(quote_len)
print(quote_start)
print(quote_ends)
print(quote_cnt_d)
print(quote_cnt_z)