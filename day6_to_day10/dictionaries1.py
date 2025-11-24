"""Figure out on how to prit 'Lille' from the nested list
called travel_log."""

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "German": ["Stuttgat", "Berlin"]
}


for key in travel_log:
    for city in travel_log[key]:
        if city == "Lille":
            print(city)


