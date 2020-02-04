def date_pharser(date):  
    
    """This function takes a list of datetime strings and converts it into a list of strings with only the date."""
    
    new_dates = []

    for item in dates:  
        a = item[:10]
        new_dates.append(a)

    return new_dates

