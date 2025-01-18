# Day 9 - Nested Data Structures
# This file demonstrates different ways to nest data structures in Python

#--------------------
# Simple Dictionary
#--------------------

# Dictionary mapping countries to capitals
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#--------------------
# Dictionary in Dictionary
#--------------------

# Dictionary containing nested dictionaries with multiple values
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],  # List inside nested dictionary
        "total_visits": 12  # Integer value
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

#--------------------
# List of Dictionaries
#--------------------

# List containing dictionaries for more flexible data structure
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],  # List inside dictionary
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]
