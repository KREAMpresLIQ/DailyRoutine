# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Dortmund"]

}

print(travel_log)

# Nesting Dictionary in a Dictionary

travel_log_dict = {
    "France": {"capital": "Paris", "country": "Dijon", "city": "Lille"},
    "Germany": {"capital": "Berlin", "country": "Hamburg", "city": "Dortmund"},
    "Hungary": {"cities_visited": ["Budapest, Szeged, Debrecen"], "total_visits": 3,
                "not_visited": ["Salgotarjan, Pecs, Gyor, Kecskemet"]}
}

print(travel_log_dict)

# Nesting Dictionary in a List

travel_list_dict = [
    {
        "country": "France",
        "cities_visited": ["Paris, Lille, Dijon"],
        "total_visits": 3
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin, Hamburg, Dortmund, Heidelberg"],
        "total_visits": 4
    },
]

print(travel_list_dict)
