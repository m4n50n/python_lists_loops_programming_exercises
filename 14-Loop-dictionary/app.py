spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

# Your code here
new_list = [["love", "amor"], ["code", "codigo"], ["smart", "inteligente"]]
for element in new_list:
        spanish_translations[element[0]] = element[1]

# Don't touch the code below
print("Translation", spanish_translations["dog"])
print(spanish_translations)
