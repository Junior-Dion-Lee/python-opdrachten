__version__ = "0.0.1"
__maintainer__ = " Junior Lee "
__status__ = "Development of Production"
# Dit bestand wordt aangeroepen en via een python commando uitgevoerd.
# In Python3 is het gebruik hiervan niet meer verplicht.
#if __name__ == "__main__":
# Hier de hoofdcode

q = """welkom bij rekenen !
voer twee gehele getallen in."""

getal1 = int(input("geef een eerste getal?"))
getal2 = int(input("geef een tweede getal?"))
print(q)
print("getal1 " + str(getal1))
print("getal2 " + str(getal2))

p = getal1 + getal2
m = getal1 - getal2
k = getal1 * getal2
g = getal1 / getal2

print(f"de som van   {getal1} en   {getal2} is  {p}")
print(f"het verschil van  {getal1} en   {getal2} is  {m}")
print(f"het product van   {getal1} en   {getal2} is {k}")
print(f"de deling van  {getal1} en {getal2} is {g}")