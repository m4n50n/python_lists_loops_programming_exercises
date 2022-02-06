all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

resulting_names = list(filter(lambda name: name.lower()[0] == "r", all_names))

print(resulting_names)
