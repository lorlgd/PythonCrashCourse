def get_formatted_city_name(city, country, population=""):
    formatted_cityname = f"{city}, {country}".title()
    if population:
        return f"{formatted_cityname} - population {population}."
    else:
        return f"{formatted_cityname}"
