import random


woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

MogelijkeLetters = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"

GeheimWoord = random.choice(woordenlijst)
lengtewoord = len(GeheimWoord)
streepjes = [" - "] *lengtewoord

print("Welkom bij galgje!")
print("Raad de letters van het woord en als je het woord denkt te weten,") 
print("typ het dan in.")
print()
print("Het woord heeft " + str(lengtewoord) + " letters.")
print(''.join(streepjes))