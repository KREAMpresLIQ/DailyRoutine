travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above
# Finally click "Run" to execute the tests

def add_new_country(country_name, visited_times, visited_cities):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = visited_times
    new_country["cities"] = visited_cities
    travel_log.append(new_country)


#  Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
