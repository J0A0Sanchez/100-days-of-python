
travel_log ={
    "France": {
        "cities_visited":  ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "German": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}


#print(travel_log)
"""Print stuttgart from above dictionarie"""


#Using print:

print(travel_log["German"]["cities_visited"][2])




#Using for loop:

for country in travel_log:
    for city in travel_log[country]["cities_visited"]:
        if city == "Stuttgart":
            print(city)