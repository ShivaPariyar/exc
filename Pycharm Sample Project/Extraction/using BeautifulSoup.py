#creating a dictionary

fav_language = {
    "Anisha":["PYthon"],
    "Manish":["PHP", "JSON"],
    "Avinash": ["Java", "R", "Swift"]

    }
for name, languages in fav_language.items():
    print("Favourite Language of "+name + " is:")
    for language in languages:
        print(language)
        